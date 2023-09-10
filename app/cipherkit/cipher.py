from .cipher_Interface import CipherInterface
import base64
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

load_dotenv()

# Cryptography library documentation: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
class CipherPy(CipherInterface):
    def __init__(self, secret_key=None, salt: bytes=None, urandom=16, length=32, iterations=100000):
        print(f"Secret Key: {secret_key}")
        if self.isNull(secret_key) and os.getenv("SECRET_WORD"):
            self.secret_key = os.getenv("SECRET_WORD")
        else:
            self.secret_key = secret_key

        if not self.secret_key:
            raise ValueError("Secret key not provided and SECRET_WORD environment variable is not set.")
        
        if type(salt) is str:
            salt = salt.encode()
        salt = salt or os.urandom(urandom)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=salt,
            iterations=iterations,
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(self.secret_key.encode()))
        self.fernet = Fernet(key)

    def encrypt(self, data: str) -> str:
        encrypted_data = self.fernet.encrypt(data.encode())
        return encrypted_data.decode()

    def validate(self, encrypted_data: str, validation_data: str) -> bool:
        decrypted_data = self.fernet.decrypt(encrypted_data.encode()).decode()
        print(f"Decrypted data: {decrypted_data}")
        return decrypted_data == validation_data

    def isNull(self, data: str) -> bool:
        return data is None or data == ""
