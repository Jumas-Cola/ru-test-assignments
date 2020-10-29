import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def key_from_password(password: str) -> bytes:
    """ Generates key from password-string.  """
    password = password.encode()
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def encrypt(password: str, message: bytes) -> bytes:
    """ Encrypts message with password.  """
    f = Fernet(key_from_password(password))
    return f.encrypt(message)


def decrypt(password: str, cipher: bytes) -> bytes:
    """ Decrypts cipher by password. """
    f = Fernet(key_from_password(password))
    return f.decrypt(cipher)

