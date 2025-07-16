# iot-temperatura-avicola
Sistema IoT para monitoreo de temperatura y humedad en granjas avícolas

Este repositorio contiene el código fuente del proyecto desarrollado para el Trabajo Fin de Máster (TFM), cuyo objetivo es implementar un sistema IoT de bajo costo para el monitoreo ambiental (temperatura y humedad) en espacios de almacenamiento de alimentos en pequeñas granjas avícolas.

## Descripción del proyecto

El sistema está basado en una **Raspberry Pi 4**, conectada a un sensor **DHT22**, que mide temperatura y humedad en tiempo real. Los datos se envían automáticamente a la plataforma en la nube **ThingSpeak**, y también se almacenan localmente en un archivo `.csv`.

El sistema permite a pequeños productores monitorear condiciones críticas que afectan la calidad de los alimentos balanceados (como el morocho) y, por tanto, la productividad de las aves.

## Tecnologías utilizadas

- **Sensor:** DHT22 (Temperatura y Humedad)
- **Plataforma IoT:** ThingSpeak
- **Lenguaje de programación:** Python 3
- **Plataforma hardware:** Raspberry Pi 4 Model B
- **Librerías:**  
  - `adafruit-circuitpython-dht`  
  - `board`, `digitalio`  
  - `requests`  
  - `time`, `csv`

## Ejecución del sistema

1. Conecta el sensor DHT22 al pin GPIO 4 de la Raspberry Pi.
2. Instala las dependencias:

```bash
pip3 install adafruit-circuitpython-dht requests

