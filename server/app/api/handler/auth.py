from fastapi import APIRouter
from app.api.schema import auth

router = APIRouter()


@router.post("/access-token", response_model=auth.Token)
async def login_access_token(login_request: auth.LoginRequest) -> auth.Token:
    return auth.Token(
        access_token=login_request.email + login_request.password, token_type="bearer"
    )
