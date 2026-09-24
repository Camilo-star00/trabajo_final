from pydantic import BaseModel, Field

class ServicioCreate(BaseModel):
    nombre: str = Field(..., example="Mantenimiento General")
    precio: float = Field(..., example=150000.0)

class ServicioResponse(ServicioCreate):
    id: int