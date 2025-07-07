from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
from backend.routers.auth import get_current_user_from_cookie
from backend.models import User, File
from backend.database import db_dependency
import os
from sqlalchemy.exc import SQLAlchemyError
from backend.document_parser import parse_pdf

UPLOAD_DIR = "files"

os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter(prefix="/files", tags=["files"])

class FileMetadataResponse(BaseModel):
    id: uuid.UUID
    name: str
    content_type: str
    size: int

@router.get("/", response_model=list[FileMetadataResponse])
async def list_files(
    current_user: Annotated[User, Depends(get_current_user_from_cookie)],
    db: db_dependency,
):
    files = db.query(File).filter(File.user_id == current_user.id).all()
    return files

@router.post("/", response_model=FileMetadataResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile,
    current_user: Annotated[User, Depends(get_current_user_from_cookie)],
    db: db_dependency,
):
    try:
        content = await file.read()
        new_file = File(
            user_id=current_user.id,
            name=file.filename,
            content_type=file.content_type,
            size=len(content),
        )
        db.add(new_file)
        db.commit()
        db.refresh(new_file)

        file_path = os.path.join(UPLOAD_DIR, str(new_file.id))
        with open(file_path, "wb") as f:
            f.write(content)
        return new_file
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating file to records: {e}")
    except Exception as e:
        if "new_file" in locals() and new_file.id:
            db.delete(new_file)
            db.commit()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error uploading file: {e}")

@router.get("/{file_id}/download")
async def download_file(
    file_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user_from_cookie)],
    db: db_dependency,
):
    try:
        file = db.query(File).filter(File.id == file_id).first()
        if not file:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
        if file.user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this file")
        file_path = os.path.join(UPLOAD_DIR, str(file.id))
        if not os.path.exists(file_path):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
        return FileResponse(
            path=file_path, media_type=file.content_type, filename=file.name
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error retrieving file: {e}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error retrieving file: {e}")

@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(
    file_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user_from_cookie)],
    db: db_dependency,
):
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    if file.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this file")
    try:
        db.delete(file)
        db.commit()
        file_path = os.path.join(UPLOAD_DIR, str(file.id))
        if os.path.exists(file_path):
            os.remove(file_path)
        return None
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error deleting file from records: {e}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error deleting file: {e}")

@router.post("/{file_id}/parse")
async def parse_file(
    file_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user_from_cookie)],
    db: db_dependency,
):
    file = db.query(File).filter(File.id == file_id).first()

    # Check if file exists and is owned by the user
    if not file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    if file.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this file")

    # Check if file exists in the upload directory
    file_path = os.path.join(UPLOAD_DIR, str(file.id))
    if not os.path.exists(file_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    # Read the file
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()

    # Parse the file
    parsed_document = await parse_pdf(pdf_bytes)
    return parsed_document
