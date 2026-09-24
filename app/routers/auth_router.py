from fastapi import APIRouter
from app.schemas.auth_schema import LoginSchema
from app.services.auth_service import AuthService

router = APIRouter()
service = AuthService()

@router.post("/login")
def login(payload: LoginSchema):
    return service.login(payload.usuario, payload.password)