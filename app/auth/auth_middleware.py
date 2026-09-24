from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer(auto_error=False)

def verificar_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    # Acepta absolutamente cualquier token sin verificar JWT ni clave
    return {"usuario": "usuario_prueba", "status": "autorizado"}