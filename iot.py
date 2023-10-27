import time
import stomp
import random

# Configuración de la conexión a ActiveMQ
conn = stomp.Connection([('localhost', 61613)]) 
conn.connect()

# Emulación de un dispositivo IoT
while True:
    # Genera datos aleatorios de temperatura y humedad
    temperatura = round(random.uniform(20.0, 30.0), 2)
    humedad = round(random.uniform(40.0, 70.0), 2)

    sensor_data = {
        "temperatura": temperatura,
        "humedad": humedad,
    }

    # Publica los datos en una cola de ActiveMQ
    conn.send(body=str(sensor_data), destination='/queue/IoTDeviceData')

    print(f"Publicado: {sensor_data}")

    time.sleep(5)  # Emula un intervalo de publicación


conn.disconnect()
