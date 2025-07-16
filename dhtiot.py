# Importación de librerías necesarias
import time
import board
import adafruit_dht
import requests
import csv
from datetime import datetime

# Configuración del pin GPIO donde está conectado el sensor DHT22
DHT_PIN = board.D4

# Configuración del canal de ThingSpeak
THING_SPEAK_URL = 'https://api.thingspeak.com/update'
API_KEY = 'B9VSEXZ******9HY'

# Archivo local para registro de datos
CSV_FILE = '/home/usuario/iot_dht22/registros.csv'

# Intervalo de tiempo entre lecturas (en segundos)
INTERVALO_SEGUNDOS = 30

# Configuración del sensor
dht_device = adafruit_dht.DHT22(DHT_PIN)

print("Iniciando monitoreo...")

while True:
    try:
        # Captura de datos desde el sensor
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        # Validación de los datos capturados
        if temperature is not None and humidity is not None:
            # Impresión en consola
            print(f"Temperatura: {temperature:.2f} °C  |  Humedad: {humidity:.2f} %")

            # Envío de datos a ThingSpeak
            payload = {'api_key': API_KEY, 'field1': temperature, 'field2': humidity}
            response = requests.get(THING_SPEAK_URL, params=payload)

            # Registro en archivo CSV
            with open(CSV_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.now().isoformat(), temperature, humidity])

        else:
            print("Error: Lectura no válida del sensor")

    except Exception as e:
        print(f"Error durante la lectura o envío: {e}")

    # Esperar antes de la siguiente lectura
    time.sleep(INTERVALO_SEGUNDOS)
