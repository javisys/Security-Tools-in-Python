#Javi_16018 - Mod 23/10/2023
import socket, sys, argparse

# Runs through each port from 1 to 65535
def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            result = s.connect_ex((ip, port))
            type_service = port_name_service(port)

            if result == 0:
                print(f"{ip} : Open port: {port}, Service: {type_service}", file=sys.stdout)

            # Close the socket
            s.close()

        except: continue

# Obtains the service name if available
def port_name_service(num_port):
    try:
        service_name = socket.getservbyport(num_port)
        return service_name
    except:
        return "unknown"

# ------------------------------------------------------------------------------------->

# Script arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', metavar='[x.x.x.x]', help='ip address')
parser.add_argument('-p', metavar='[0:65535]', help='port range')
args = parser.parse_args()

# Port arguments
if args.p:
    try:
        start_port, end_port = args.p.split(":"); start_port, end_port = int(start_port), int(end_port)

        # Stops the code if the port range is incorrect
        if   start_port > 65535 or end_port > 65535 : print("Invalid port range", file=sys.stderr); sys.exit(1)
        elif start_port > end_port                  : print("Initial range greater than final range", file=sys.stderr); sys.exit(1)

    except:
        print(f"Invalid port range", file=sys.stderr); sys.exit(1)

# IP Arguments
if args.i: ip_address = args.i


# Port scanning is performed
try:
    scan_ports(ip_address, start_port, end_port)
except:
    print(f"Error: Failed to execute the command, please check the arguments, use --help", file=sys.stderr); sys.exit(1)
