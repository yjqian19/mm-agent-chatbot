from fastapi import FastAPI
from backend.database import init_db
from backend.routes.users import router as users_router
from backend.routes.auth import router as auth_router
from backend.routes.file import router as file_router

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "OK"}

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(file_router)
