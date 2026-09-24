import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Misma clave usada en el middleware
JWT_SECRET = os.getenv("JWT_SECRET", "clave_super_secreta_y_larga_de_mas_de_32_caracteres_12345")
ALGORITHM = "HS256"

class AuthService:
    def login(self, usuario: str, password: str):
        payload = {
            "sub": "1",
            "usuario": usuario,
            "exp": datetime.utcnow() + timedelta(days=365)
        }
        
        # Genera el token usando JWT_SECRET
        token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
        
        return {
            "mensaje": f"Bienvenido {usuario}, inicio de sesión exitoso",
            "token": token,
            "token_type": "bearer"
        }