# Javier Ferrándiz Fernández - 22/12 
import os
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding


# Generate a private key with the RSA algorithm
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)


# Convert private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)


# Write the private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_pem)

# Generate a public key from the private key
public_key = private_key.public_key()


# Serialize the public key to SSH format
ssh_key = public_key.public_bytes(
    encoding=serialization.Encoding.OpenSSH,
    format=serialization.PublicFormat.OpenSSH
)

# Write the public key to a file
with open("public_key.ssh", "wb") as f:
    f.write(ssh_key)

