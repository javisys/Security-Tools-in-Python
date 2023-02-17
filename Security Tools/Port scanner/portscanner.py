#Javi_16018
import socket

# IP address of the host you want to scan
ip = "192.168.1.1"

# Runs through each port from 1 to 65535
for port in range(1, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"Puerto abierto: {port}")

    # Close the socket
    s.close()
