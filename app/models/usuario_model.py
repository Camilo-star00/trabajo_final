from app.database.db import get_db_connection

class UsuarioModel:
    def get_by_usuario(self, usuario: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user