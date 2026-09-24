from app.models.servicio_model import ServicioModel

class ServicioService:
    def __init__(self):
        self.model = ServicioModel()

    def obtener_todos(self):
        return self.model.get_all()

    def obtener_por_id(self, servicio_id: int):
        return self.model.get_by_id(servicio_id)

    def crear(self, nombre: str, precio: float):
        # Permite crear con cualquier precio o dato
        return self.model.create(nombre, precio)

    def actualizar(self, servicio_id: int, nombre: str, precio: float):
        return self.model.update(servicio_id, nombre, precio)

    def eliminar(self, servicio_id: int):
        self.model.delete(servicio_id)
        return {"message": "Eliminado correctamente"}