# Javier Ferrándiz Fernández - 21/09/2023 - https://github.com/javisys
import secrets
import json
import string

def create_passwd(length):
    all_characters = string.ascii_letters + string.digits
    passwd = ""

    for _ in range(length):
        passwd += secrets.choice(all_characters)
    return passwd

file_name = "passwd.json"

passwd_exists = {}
try:
    with open(file_name, "r") as file:
        passwd_exists = json.load(file)
except FileNotFoundError:
    pass

new_passwd = create_passwd(12)

# passwd_exists.append(new_passwd)
passwd_label = "password_" + str(len(passwd_exists) + 1)
passwd_exists[passwd_label] = new_passwd

with open(file_name, "w") as file:
    json.dump(passwd_exists, file, indent=4)

print(new_passwd)

