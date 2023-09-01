from serial import Serial as serial
from time import sleep

# Mensaje de bienvenida
print("Conectando puerto serie...")

# Variable para puerto serie
ser = None

try:
	# Abro el puerto serie en ttyS0 a 115200
	ser = serial("/dev/ttyS0", 115200)
	ser.write("Raspberry Pi esta escuchando. Escriba algo por la consola\r\n\n".encode('utf-8'))
	print("Puerto serie abierto en /dev/ttyS0. [Ctrl + C] para terminar")

except:
	print("Error al abrir puerto ttyS0. No hay nada conectado")
	print("[Ctrl + C] para terminar")

try:
	while True:
		# Leo los bytes disponibles
		recv = ser.read()
		# Mando de vuelta el mensaje
		ser.write(recv)
		# Imprimo por consola de Python lo que se recibio
		print(f"{recv.decode('utf-8')}", end="", flush=True)

except KeyboardInterrupt:
	print()
	print("Programa terminado")
