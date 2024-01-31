import os
import sys
import time
import atexit
from firebase import firebase

# Configuración de la conexión a la Realtime Database
firebase_url = 'https://pc-logger-default-rtdb.firebaseio.com/'
firebase_db = firebase.FirebaseApplication(firebase_url, None)

# Función para registrar el evento en la base de datos
def log_event(state):
    timestamp = time.time()
    fecha_hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    data = {'estado': state, 'fecha_hora': fecha_hora}
    firebase_db.put('/Login/', '0', data)

# Función para ejecutar al apagar la aplicación
def exit_handler():
    log_event('apagada')

# Registrar el evento al iniciar la aplicación
log_event('encendida')

# Registrar la función para ejecutar al apagar la aplicación
atexit.register(exit_handler)

try:
    while True:
        # Puedes personalizar esta parte dependiendo del sistema operativo
        if sys.platform.startswith('win'):
            if os.system('shutdown /s /t 1') == 0:  # Apagar la PC
                break
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            if os.system('sudo shutdown now') == 0:  # Apagar la PC
                break
        else:
            print("Sistema operativo no compatible.")
            break
except KeyboardInterrupt:
    # Registrar el evento al cerrar la aplicación manualmente
    log_event('apagada_manualmente')
