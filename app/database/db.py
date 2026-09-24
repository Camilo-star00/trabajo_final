import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        os.getenv("DATABASE_URL"),
        cursor_factory=RealDictCursor
    )

def init_db():
    tables_sql = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        usuario VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS servicios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(150) NOT NULL,
        precio NUMERIC(10, 2) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS solicitud_servicio (
        id SERIAL PRIMARY KEY,
        id_servicio INT REFERENCES servicios(id),
        fecha VARCHAR(50) NOT NULL,
        cliente VARCHAR(150) NOT NULL
    );

    INSERT INTO usuarios (usuario, password) 
    VALUES ('camilo', '123456')
    ON CONFLICT (usuario) DO NOTHING;
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(tables_sql)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tablas verificadas/creadas con éxito.")
    except Exception as e:
        print(f"Error inicializando tablas: {e}")