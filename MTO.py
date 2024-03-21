
import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Manejo de errores
class EmptyMessage(Exception):
    """No se puede encriptar un mensaje vacío""" 

class MinimunCharacters(Exception):
    """La key debe contener 4 caracteres mínimo""" 

class IncorrectKey(Exception):
    """La key está incorrecta"""

# Lógica para encriptar y desencriptar
class EncryptionEngine:
    # Características que debe tener la llave
    def __init__(self, key): 
        if not key:
            raise ValueError("La key no puede estar vacía.")
        if isinstance(key, int):
            self.key = key
        elif isinstance(key, str):
            if len(key) < 4:
                raise MinimunCharacters("La key debe contener al menos 4 caracteres.")
            self.key = self.get_key_value(key)
        else:
            raise ValueError("La key debe ser un número entero o una cadena de letras.")
    
    def encrypt(self, mensaje):
        if not mensaje:
            raise EmptyMessage("No se puede encriptar un mensaje vacío.")

        cipher = Cipher(algorithms.AES(self.key.to_bytes(32, byteorder='big')),
                        modes.ECB(),
                        backend=default_backend())

        encryptor = cipher.encryptor()

        encrypted_message = encryptor.update(mensaje.encode('utf-8')) + encryptor.finalize()
        return encrypted_message

    def decrypt(self, encrypted_message, key=None):
        if not encrypted_message:
            raise ValueError("El mensaje no ha sido encriptado previamente o está vacío.")

        if key is None:
            key = self.key  # Utiliza la key guardada si no se proporciona una key

        if key != self.key:
            raise IncorrectKey("La clave proporcionada no coincide con la clave utilizada para encriptar el mensaje.")

        cipher = Cipher(algorithms.AES(key.to_bytes(32, byteorder='big')),
                        modes.ECB(),
                        backend=default_backend())

        decryptor = cipher.decryptor()

        try:
            decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
            return decrypted_message.decode('utf-8')
        except ValueError:
            raise ValueError("El mensaje encriptado está corrupto o ha sido modificado.")

    def get_key_value(self, key):
        # Convertir cada letra de la key a su valor numérico y sumarlos
        return sum(ord(letra) for letra in key)

def has_sinogram(mensaje):
    # Rangos Unicode de sinogramas
    sinogram_ranges = [
        (0x4E00, 0x9FFF),  # Rango básico de sinogramas comunes
        (0x3400, 0x4DBF),  # Rango de sinogramas extendidos A
        (0x20000, 0x2A6DF),  # Rango de sinogramas extendidos B
        (0x2A700, 0x2B73F),  # Rango de sinogramas extendidos C
        (0x2B740, 0x2B81F),  # Rango de sinogramas extendidos D
        (0x2B820, 0x2CEAF),  # Rango de sinogramas extendidos E
        (0x2CEB0, 0x2EBEF),  # Rango de sinogramas extendidos F
        (0xF900, 0xFAFF),  # Rango de sinogramas compatibles con ideogramas CJK
        (0x2F800, 0x2FA1F)  # Rango de sinogramas suplementarios
    ]