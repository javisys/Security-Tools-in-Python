# Javier Ferrándiz Fernández - 21/09/2023 - https://github.com/javisys
import secrets
import string

def create_passwd(length):
    all_characters = string.ascii_letters + string.digits
    passwd = ""

    for _ in range(length):
        passwd += secrets.choice(all_characters)
    return passwd

file_name = "passwd.txt"

passwd_exists = []
try:
    with open(file_name, "r") as file:
        passwd_exists = file.read().splitlines()
except FileNotFoundError:
    pass

new_passwd = create_passwd(10)

passwd_exists.append(new_passwd)

with open(file_name, "w") as file:
    file.write("\n".join(passwd_exists))

print(new_passwd)

