from app.database.db import get_db_connection

class SolicitudModel:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM solicitud_servicio ORDER BY id ASC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_by_id(self, solicitud_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM solicitud_servicio WHERE id = %s", (solicitud_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def create(self, id_servicio: int, fecha: str, cliente: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO solicitud_servicio (id_servicio, fecha, cliente) VALUES (%s, %s, %s) RETURNING *",
            (id_servicio, fecha, cliente)
        )
        new_row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return new_row

    def update(self, solicitud_id: int, id_servicio: int, fecha: str, cliente: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE solicitud_servicio SET id_servicio = %s, fecha = %s, cliente = %s WHERE id = %s RETURNING *",
            (id_servicio, fecha, cliente, solicitud_id)
        )
        updated_row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return updated_row

    def delete(self, solicitud_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM solicitud_servicio WHERE id = %s RETURNING *", (solicitud_id,))
        deleted_row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_row