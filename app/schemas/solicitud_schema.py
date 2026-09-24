from pydantic import BaseModel, Field

class SolicitudCreate(BaseModel):
    id_servicio: int = Field(..., example=1)
    fecha: str = Field(..., example="2026-09-24")
    cliente: str = Field(..., example="Carlos Pérez")

class SolicitudResponse(SolicitudCreate):
    id: int