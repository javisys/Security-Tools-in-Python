import hashlib

# We first compute hashes of text strings and then of files.
# The text string for which you want to calculate the hash.
txt = "Hello World!"

# Creates a hash object using the SHA256 algorithm.
hash_object = hashlib.sha256()

# Updates the hash object with the text string.
hash_object.update(txt.encode())

# Get the hash in hexadecimal form.
hex_hash = hash_object.hexdigest()


filename = "example.txt"

hash_object2 = hashlib.sha256()

# Opens the file in binary read mode
with open(filename, 'rb') as file:
    # Reads the contents of the file in blocks
    chunk = file.read(1024)
    while chunk:
        hash_object2.update(chunk)
        chunk = file.read(1024)

hex_hash2 = hash_object2.hexdigest()

# Displays the hash.
print(hex_hash)

# Displays the file hash.
print(hex_hash2)