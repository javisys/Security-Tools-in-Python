import socket

# Dirección IP del host que quieres escanear
ip = "192.168.1.1"

# Recorre cada puerto del 1 al 65535
for port in range(1, 65536):
    # Crea un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establece un tiempo de espera de 1 segundo para evitar colgarse
    s.settimeout(1)

    # Intenta conectarse al puerto del host
    result = s.connect_ex((ip, port))

    # Si la conexión es exitosa, muestra el puerto
    if result == 0:
        print(f"Puerto abierto: {port}")

    # Cierra el socket
    s.close()
