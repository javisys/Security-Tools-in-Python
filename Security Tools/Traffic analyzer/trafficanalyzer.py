from scapy.all import *

# Function that will be executed when a packet is received.
def packet_callback(packet):
    if packet[TCP]:
        print(f"Paquete TCP de {packet[IP].src} a {packet[IP].dst}")
        print(f"Puertos: {packet[TCP].sport} -> {packet[TCP].dport}")
        print(f"Tamaño: {len(packet)} bytes")

# Starts packet capture on network interface "eth0".
sniff(iface="eth0", prn=packet_callback, filter="tcp")
