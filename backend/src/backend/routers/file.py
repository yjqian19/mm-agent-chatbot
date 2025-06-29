from typing import Annotated
from fastapi import APIRouter, Depends, status, UploadFile
from pydantic import BaseModel
import uuid
from backend.routers.auth import get_current_user
from backend.models import User
from backend.database import db_dependency

router = APIRouter(prefix="/files", tags=["files"])

class FileMetadataResponse(BaseModel):
    id: uuid.UUID
    name: str
    content_type: str
    size: int

@router.get("/", response_model=list[FileMetadataResponse])
async def list_files(
    current_user: Annotated[User, Depends(get_current_user)],
    db: db_dependency,
):
    return []

@router.post("/", response_model=FileMetadataResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile,
    current_user: Annotated[User, Depends(get_current_user)],
    db: db_dependency,
):
    pass

@router.get("/{file_id}/download")
async def download_file(
    file_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user)],
    db: db_dependency,
):
    pass

@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(
    file_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user)],
    db: db_dependency,
):
    pass
