# Javier Ferrándiz Fernández - 21/09/2023 - https://github.com/javisys
import secrets
import string

def create_passwd(length):
    all_characters = string.ascii_letters + string.digits
    passwd = ""

    for _ in range(length):
        passwd += secrets.choice(all_characters)
    return passwd

new_passwd = create_passwd(10)
print(new_passwd)


