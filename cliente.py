import time
import random
import stomp
from multiprocessing import Process

# Función para emular dispositivos IoT que generan datos aleatorios
def emulate_device(device_name, interest):
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect()
    
    while True:
        sensor_data = {
            "device_name": device_name,
            "temperatura": round(random.uniform(20.0, 30.0), 2),
            "humedad": round(random.uniform(40.0, 70.0), 2)
        }
        
        # Publica los datos en la cola
        if interest == "temperatura":
            conn.send(body=str(sensor_data), destination='/queue/TemperatureData')
        elif interest == "humedad":
            conn.send(body=str(sensor_data), destination='/queue/HumidityData')

        print(f"{device_name} - Publicado: {sensor_data} ({interest})")
        time.sleep(5)

# Crea múltiples procesos 
if __name__ == '__main__':
    devices = [
        ("Device1", "temperatura"),
        ("Device2", "temperatura"),
        ("Device3", "humedad"),
        ("Device4", "humedad")
    ]
    
    processes = []
    for device_name, interest in devices:
        process = Process(target=emulate_device, args=(device_name, interest))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
