#Javi_16018 - Mod 23/10/2023
import socket

# Runs through each port from 1 to 65535
def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"Open port: {port}")

    # Close the socket
    s.close()


# IP address of the host you want to scan
ip = "192.168.1.1"

# Define the range of ports you want to scan
start_port = 1
end_port = 65535

scan_ports(ip, start_port, end_port)
