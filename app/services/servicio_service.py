from fastapi import HTTPException, status
from app.models.servicio_model import ServicioModel

class ServicioService:
    def __init__(self):
        self.model = ServicioModel()

    def obtener_todos(self):
        return self.model.get_all()

    def obtener_por_id(self, servicio_id: int):
        servicio = self.model.get_by_id(servicio_id)
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El servicio con ID {servicio_id} no fue encontrado"
            )
        return servicio

    def crear(self, nombre: str, precio: float):
        if precio <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El precio del servicio debe ser mayor a 0"
            )
        return self.model.create(nombre, precio)

    def actualizar(self, servicio_id: int, nombre: str, precio: float):
        self.obtener_por_id(servicio_id)  # Valida existencia antes de actualizar
        if precio <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El precio del servicio debe ser mayor a 0"
            )
        return self.model.update(servicio_id, nombre, precio)

    def eliminar(self, servicio_id: int):
        self.obtener_por_id(servicio_id)  # Valida existencia antes de eliminar
        self.model.delete(servicio_id)
        return {"mensaje": f"Servicio con ID {servicio_id} eliminado exitosamente"}