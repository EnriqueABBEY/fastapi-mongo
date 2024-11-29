from fastapi import FastAPI

from src.v1.auth.routes import router as auth_routes

app = FastAPI()

app.include_router(auth_routes, prefix="/auth", tags=["auth"])
