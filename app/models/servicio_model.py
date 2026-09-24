from app.database.db import get_db_connection

class ServicioModel:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servicios ORDER BY id ASC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_by_id(self, servicio_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servicios WHERE id = %s", (servicio_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def create(self, nombre: str, precio: float):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO servicios (nombre, precio) VALUES (%s, %s) RETURNING *",
            (nombre, precio)
        )
        new_row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return new_row

    def update(self, servicio_id: int, nombre: str, precio: float):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE servicios SET nombre = %s, precio = %s WHERE id = %s RETURNING *",
            (nombre, precio, servicio_id)
        )
        updated_row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return updated_row

    def delete(self, servicio_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM servicios WHERE id = %s RETURNING *", (servicio_id,))
        deleted_row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_row