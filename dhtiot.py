#Importación de librerías necesarias
import time
import csv
import board
import adafruit_dht
import requests
from datetime import datetime

# Configuración del pin GPIO donde está conectado el sensor DHT22
DHT_PIN = board.D4  # GPIO4

# Configuración del canal de ThingSpeak
THING_SPEAK_URL = 'https://api.thingspeak.com/update'
THING_SPEAK_API_KEY = 'B9VXXXXXXXXXX9HY'

# Archivo local para registro de datos
CSV_FILE = '/home/fherpico/iot_dht22/dhtiot_log.csv'

# Intervalo de tiempo entre lecturas (en segundos)
INTERVALO_SEGUNDOS = 20

# Umbrales
TEMP_MAX = 15.0
TEMP_MIN = 7.0
HUMEDAD_MAX = 80.0
HUMEDAD_MIN = 40.0

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
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Impresión en consola
            print(f"{now} - Temp: {temperature:.1f}°C, Humedad: {humidity:.1f}%")

            if temperature > TEMP_MAX:
                print("ALERTA: Temperatura alta")
            elif temperature < TEMP_MIN:
                print("ALERTA: Temperatura baja")

            if humidity > HUMEDAD_MAX:
                print("ALERTA: Humedad alta")
            elif humidity < HUMEDAD_MIN:
                print("ALERTA: Humedad baja")

            # Registro en archivo CSV
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([now, temperature, humidity])

            # Envío de datos a ThingSpeak
            payload = {
                'api_key': THING_SPEAK_API_KEY,
                'field1': temperature,
                'field2': humidity
            }
            response = requests.get(THING_SPEAK_URL, params=payload)
            print("Enviado a ThingSpeak. Código:", response.status_code)
        else:
            print("Error de lectura del sensor.")
    except Exception as e:
        print("Error:", e)
    
# Espera antes de la siguiente lectura   
 time.sleep(INTERVALO_SEGUNDOS)
