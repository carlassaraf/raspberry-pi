from gpiozero import DigitalOutputDevice as Output
from time import sleep

# Mensaje de ejemplo
print("Blinky en GPIO25 corriento [Ctrl + C para salir]")

# Creo una isntancia de una salida asociada al GPIO25
led = Output(25)

try:
    while True:
        # Leo el estado y lo niego para blinkear
        led.value = not led.value
        # Demora
        sleep(.5)

# Mensaje de salida cuando se interrumpe el programa con Ctrl + C
except KeyboardInterrupt:
    print()
    print("Programa finalizado")