import sqlite3

def get_connection():
    conn = sqlite3.connect("Residentevil.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()

def initDb():
    conn = sqlite3.connect("Residentevil.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS armas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, potencia INTEGER, velocidad INTEGER, capacidad INTEGER, precio REAL)"
    )
    conn.commit()
    conn.close()