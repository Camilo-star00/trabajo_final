import jwt
import os
from fastapi import Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv

load_dotenv()

# Clave secreta definida en tu archivo .env
JWT_SECRET = os.getenv("JWT_SECRET", "clave_super_secreta_y_larga_de_mas_de_32_caracteres_12345")
ALGORITHM = "HS256"

security = HTTPBearer()

def verificar_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    try:
        # Decodifica y valida la firma y expiración del token
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token ha expirado. Por favor, inicia sesión de nuevo."
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o no proporcionado"
        )