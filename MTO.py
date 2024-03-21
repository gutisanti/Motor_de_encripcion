from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

class EncryptionError(Exception):
    pass

class DecryptionError(Exception):
    pass

def encrypt_message(message, password):
    try:
        # Definir una sal (salt) y un factor de iteración
        salt = b'salt_'
        iterations = 100_000
        
        # Derivar una clave a partir de la contraseña
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        
        # Agregar padding al mensaje
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()

        # Inicializar el cifrador
        cipher = Cipher(algorithms.AES(key), modes.CBC(b'0' * 16), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Encriptar el mensaje
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Devolver el texto cifrado como base64
        return base64.b64encode(ciphertext).decode()
    except Exception as e:
        raise EncryptionError("Error al encriptar el mensaje") from e

def decrypt_message(ciphertext, password):
    try:
        # Decodificar el texto cifrado de base64
        ciphertext = base64.b64decode(ciphertext.encode())
        
        # Derivar la clave de la contraseña
        salt = b'salt_'
        iterations = 100_000
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        
        # Inicializar el descifrador
        cipher = Cipher(algorithms.AES(key), modes.CBC(b'0' * 16), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Desencriptar el mensaje y quitar el padding
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        
        # Devolver el mensaje descifrado
        return unpadded_data.decode()
    except Exception as e:
        raise DecryptionError("Error al desencriptar el mensaje") from e





