from fastapi import APIRouter, Depends
from app.schemas.servicio_schema import ServicioCreate, ServicioResponse
from app.services.servicio_service import ServicioService
from app.auth.auth_middleware import verificar_token

router = APIRouter(dependencies=[Depends(verificar_token)])
service = ServicioService()

@router.get("/", response_model=list[ServicioResponse])
def listar_servicios():
    return service.obtener_todos()

@router.get("/{servicio_id}", response_model=ServicioResponse)
def obtener_servicio(servicio_id: int):
    return service.obtener_por_id(servicio_id)

@router.post("/", response_model=ServicioResponse)
def crear_servicio(payload: ServicioCreate):
    return service.crear(payload.nombre, payload.precio)

@router.put("/{servicio_id}", response_model=ServicioResponse)
def actualizar_servicio(servicio_id: int, payload: ServicioCreate):
    return service.actualizar(servicio_id, payload.nombre, payload.precio)

@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int):
    return service.eliminar(servicio_id)