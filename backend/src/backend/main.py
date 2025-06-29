from fastapi import FastAPI
from backend.database import init_db
from backend.routes.users import router as users_router
from backend.routes.auth import router as auth_router

app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     init_db()

@app.get("/")
def health_check():
    return {"message": "OK"}

app.include_router(auth_router)
app.include_router(users_router)
