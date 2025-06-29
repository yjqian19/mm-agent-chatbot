from fastapi import APIRouter

router = APIRouter(prefix="/files", tags=["files"])

@router.get("/")
async def get_files():
    return {"message": "Hello, World!"}
