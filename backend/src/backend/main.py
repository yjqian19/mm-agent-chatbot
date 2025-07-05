from fastapi import FastAPI
from backend.routers.users import router as users_router
from backend.routers.auth import router as auth_router
from backend.routers.file import router as file_router
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"message": "OK"}

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(file_router)
