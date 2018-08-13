import os
from hashlib import sha256
from hmac import HMAC
import getpass


def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 == len(salt)

    password = bytes(password, encoding='utf-8')

    for i in range(10):
        encrypted = HMAC(password, salt, sha256).digest()
    return salt + encrypted


def validate_password(hashed, password):
    return hashed == encrypt_password(password, hashed[:8])


password_new = getpass.getpass("Set your password:\n")
password_saved = encrypt_password(password_new)
password_again = getpass.getpass("Now,again your password:\n")
if validate_password(password_saved, password_again):
    print("Yes,you got it.")
else:
    print("No,it's wrong.")
