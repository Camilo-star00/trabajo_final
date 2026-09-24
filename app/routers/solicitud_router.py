from fastapi import APIRouter, Depends
from app.schemas.solicitud_schema import SolicitudCreate, SolicitudResponse
from app.services.solicitud_service import SolicitudService
from app.auth.auth_middleware import verificar_token

router = APIRouter(dependencies=[Depends(verificar_token)])
service = SolicitudService()

@router.get("/", response_model=list[SolicitudResponse])
def listar_solicitudes():
    return service.obtener_todas()

@router.get("/{solicitud_id}", response_model=SolicitudResponse)
def obtener_solicitud(solicitud_id: int):
    return service.obtener_por_id(solicitud_id)

@router.post("/", response_model=SolicitudResponse)
def crear_solicitud(payload: SolicitudCreate):
    return service.crear(payload.id_servicio, payload.fecha, payload.cliente)

@router.put("/{solicitud_id}", response_model=SolicitudResponse)
def actualizar_solicitud(solicitud_id: int, payload: SolicitudCreate):
    return service.actualizar(solicitud_id, payload.id_servicio, payload.fecha, payload.cliente)

@router.delete("/{solicitud_id}")
def eliminar_solicitud(solicitud_id: int):
    return service.eliminar(solicitud_id)