from fastapi import HTTPException, status
from app.models.solicitud_model import SolicitudModel
from app.models.servicio_model import ServicioModel

class SolicitudService:
    def __init__(self):
        self.model = SolicitudModel()
        self.servicio_model = ServicioModel()

    def obtener_todas(self):
        return self.model.get_all()

    def obtener_por_id(self, solicitud_id: int):
        solicitud = self.model.get_by_id(solicitud_id)
        if not solicitud:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"La solicitud con ID {solicitud_id} no fue encontrada"
            )
        return solicitud

    def crear(self, id_servicio: int, cliente: str, fecha: str):
        # Valida que el servicio asociado exista en la BD antes de crear la solicitud
        servicio = self.servicio_model.get_by_id(id_servicio)
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"No se puede crear la solicitud: El servicio con ID {id_servicio} no existe"
            )
        return self.model.create(id_servicio, cliente, fecha)

    def eliminar(self, solicitud_id: int):
        self.obtener_por_id(solicitud_id)  # Valida existencia antes de eliminar
        self.model.delete(solicitud_id)
        return {"mensaje": f"Solicitud con ID {solicitud_id} eliminada exitosamente"}