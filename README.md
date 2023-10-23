# Security-Tools-in-Python
Several simple projects done in Python for network monitoring for Cybersecurity and high availability. All the modules needed are in their folder with the script.

UPDATED, ADDED PASSWORD GENERATOR

BANDWIDTH
This script, made with the psutil library, obtains your bandwidth on the network interface you specify.

References
https://pypi.org/project/psutil/

CRYPTOGRAPHY
This script generates a private key with the RSA encryption algorithm of 2048, then what it does is to convert the private key to a PEM format file, we write the key to the generated file. Then we generate the public key from the private key. 
Finally we pass the public key to an SSH file and write it to a file.

References
https://pypi.org/project/cryptography/

FIREWALL RULE
This script is very customizable, as we can adjust it for our own needs, in this case I have made a rule to block ping, another rule to block RDP protocol, and the last rule allows TCP traffic from one subnet to another over port 80, in this case, the good thing about this is that you can change it to suit your needs.

References
https://pypi.org/project/python-iptables/

HASH CALCULATOR


References
https://pypi.org/project/hashlib/


