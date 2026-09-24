import uvicorn
from fastapi import FastAPI
from app.database.db import init_db
from app.routers.auth_router import router as auth_router
from app.routers.servicio_router import router as servicio_router
from app.routers.solicitud_router import router as solicitud_router

# Inicializa las tablas al arrancar
init_db()

app = FastAPI(title="Proyecto Final API", version="1.0.0")

app.include_router(auth_router, prefix="/api/auth", tags=["Autenticación"])
app.include_router(servicio_router, prefix="/api/servicios", tags=["Servicios"])
app.include_router(solicitud_router, prefix="/api/solicitudes", tags=["Solicitudes"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)