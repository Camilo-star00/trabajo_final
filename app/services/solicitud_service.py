from fastapi import HTTPException
from app.models.solicitud_model import SolicitudModel

class SolicitudService:
    def __init__(self):
        self.model = SolicitudModel()

    def obtener_todas(self):
        return self.model.get_all()

    def obtener_por_id(self, solicitud_id: int):
        solicitud = self.model.get_by_id(solicitud_id)
        if not solicitud:
            raise HTTPException(status_code=404, detail="Solicitud no encontrada")
        return solicitud

    def crear(self, id_servicio: int, fecha: str, cliente: str):
        return self.model.create(id_servicio, fecha, cliente)

    def actualizar(self, solicitud_id: int, id_servicio: int, fecha: str, cliente: str):
        actualizado = self.model.update(solicitud_id, id_servicio, fecha, cliente)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Solicitud no encontrada")
        return actualizado

    def eliminar(self, solicitud_id: int):
        eliminado = self.model.delete(solicitud_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Solicitud no encontrada")
        return {"message": "Solicitud eliminada correctamente"}