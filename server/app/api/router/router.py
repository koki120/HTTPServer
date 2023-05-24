from fastapi import APIRouter
from app.api.handler import auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/api/auth", tags=["auth"])
