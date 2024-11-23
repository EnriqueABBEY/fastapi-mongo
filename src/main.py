from fastapi import FastAPI

from src.auth.routes import router as auth_routes

app = FastAPI()

app.include_router(auth_routes, prefix="/auth", tags=["auth"])
