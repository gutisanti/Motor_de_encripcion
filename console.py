import os
from cryptography.hazmat.backends import default_backend
from MTO import EncryptionEngine, EmptyMessage, MinimunCharacters, IncorrectKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode


def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def generate_seecret_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode('utf-8'),
        iterations=100000,
        backend=default_backend()
    )
    return urlsafe_b64encode(kdf.derive(password.encode('utf-8'))) #Convierte la cadena de caracteres en una secuencia de bytes utilizando la codificación UTF-8

def main():
    # Solicitar al usuario que elija entre encriptar o desencriptar
    option = input("¿Desea enciptar (E) o desencrpitar (D) un mensaje? ").upper()

    # Validar la opción ingresada
    if option not in ["E", "D"]:
        print("Opción no válida. Por favor, ingrese 'E' para encriptar o 'D' para desencriptar")
        exit()

    # Realizar la operación seleccionada por el usuario
    if option == "E":
        message = input("Ingrese el mensaje: ")  
        password = input("Ingrese la contraseña para generar la clave: ")
        salt = os.urandom(16).hex()  # Generar un salt aleatorio, un salt es un valor aleatorio único que se agrega a los datos antes de derivar la clave.
        secret_key = generate_seecret_key(password, salt)
        my_engine = EncryptionEngine(int.from_bytes(secret_key, 'big'))
        encrypted_word = my_engine.encrypt(message)  # Aqui se encripta el mensaje
        print("mensaje encriptado:", encrypted_word)

        with open("encrypted_word.txt", "w", encoding="utf-8") as file:
            #Estas dos lineas de codigo escriben en el archivo la palabra encriptada
            file.write(f"mensaje encriptada: {encrypted_word}\n")
            file.write(f"Salt: {salt}\n")

        print("mensaje encriptado y salt guardados en 'encrypted_word.txt'.")

    elif option == "D":
        password = input("Ingrese la contraseña para generar la clave: ")

        try:
            with open("encrypted_word.txt", "r", encoding="utf-8") as file:
                lines = file.readlines() #lee las lineas del archivo de texto generado anteriormente
                salt = lines[1].split(":")[1].strip()
        except FileNotFoundError:
            print("No se encontró el file 'encrypted_word.txt'.")
            exit()
        except (ValueError, IndexError):
            print("Error al leer el salt almacenado.")
            exit()

        secret_key = generate_seecret_key(password, salt)
        my_engine = EncryptionEngine(int.from_bytes(secret_key, 'big')) #Se está creando una instancia de esta EncryptionEngine y se está inicializando con una clave

        encrypted_word = lines[0].split(":")[1].strip()
        try:
            decrypted_word = my_engine.decrypt(encrypted_word)
            print("mensaje desencriptado:", decrypted_word)
        except (ValueError, IncorrectKey, EmptyMessage, MinimunCharacters) as error:
            print(f"Error al dessencriptar: {error}")

if __name__ == "__main__":
    main()

