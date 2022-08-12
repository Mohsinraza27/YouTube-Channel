import string
import secrets

Characters = string.ascii_letters+string.digits
password = ''.join(secrets.choice(Characters)
            for i in range(10))

print(password)
