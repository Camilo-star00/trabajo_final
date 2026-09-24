import jwt
from datetime import datetime, timedelta

class AuthService:
    def login(self, usuario: str, password: str):
        payload = {
            "sub": "1",
            "usuario": usuario,
            "exp": datetime.utcnow() + timedelta(days=365)
        }
        
        token = jwt.encode(payload, "clave_cualquiera_1234567890_super_larga", algorithm="HS256")
        
        return {
            "mensaje": f"Bienvenido {usuario}, inicio de sesión exitoso",
            "token": token,
            "token_type": "bearer"
        }