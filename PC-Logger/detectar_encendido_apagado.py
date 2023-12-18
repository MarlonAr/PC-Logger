import os
import mysql.connector
from datetime import datetime
import ctypes

# Configura la conexión a la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'labcom,2015',
    'database': 'logger_register'
}

# Función para registrar la fecha y hora en la base de datos
def registrar_estado(estado):
    connection = None  # Inicializamos la variable connection antes del bloque try

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Inserta la fecha y hora actual en la tabla 'registro'
        cursor.execute("INSERT INTO registro (estado, fecha_hora) VALUES (%s, %s)", (estado, datetime.now()))

        connection.commit()
        cursor.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

# Obtiene el estado actual del sistema
def obtener_estado():
    is_desktop = ctypes.windll.user32.GetForegroundWindow() != 0
    return "Encendida" if is_desktop else "Apagada"

# Registra el estado actual en la base de datos
registrar_estado(obtener_estado())