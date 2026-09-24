from fastapi import HTTPException
from app.models.servicio_model import ServicioModel

class ServicioService:
    def __init__(self):
        self.model = ServicioModel()

    def obtener_todos(self):
        return self.model.get_all()

    def obtener_por_id(self, servicio_id: int):
        servicio = self.model.get_by_id(servicio_id)
        # Si no existe en la BD, lanzamos un 404 en lugar de devolver None
        if not servicio:
            raise HTTPException(status_code=404, detail="Servicio no encontrado")
        return servicio

    def crear(self, nombre: str, precio: float):
        return self.model.create(nombre, precio)

    def actualizar(self, servicio_id: int, nombre: str, precio: float):
        actualizado = self.model.update(servicio_id, nombre, precio)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Servicio no encontrado")
        return actualizado

    def eliminar(self, servicio_id: int):
        eliminado = self.model.delete(servicio_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Servicio no encontrado")
        return {"message": "Servicio eliminado correctamente"}