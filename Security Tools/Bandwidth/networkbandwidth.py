#Javi_16018 - 10/12/2022
import psutil

# Obtain the information of the network interface "eth0" or your network interface that you use.
network_info = psutil.net_io_counters(pernic=True)["eth0"]

# Get the bandwidth used in bytes
bandwidth_used = network_info.bytes_sent + network_info.bytes_recv

# Convert to megabytes
bandwidth_used_mb = bandwidth_used / 1024 / 1024

print(f"The following have been used {bandwidth_used_mb:.2f} MB of bandwidth.")

# To obtain in gigabytes
bandwidth_used_X = bandwidth_used / 1024 / 1024 / 1024  

# To obtain in kilobytes
bandwidth_used_X = bandwidth_used / 1024


