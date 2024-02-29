import string

class EmptyMessage(Exception):
    """No se puede encriptar un mensaje vacio"""
class MotorEncriptacion:
    
    def __init__(self, clave):
        if not clave:
            raise ValueError("La clave no puede estar vacía.")
        
        if isinstance(clave, int):
            self.clave = clave
        elif isinstance(clave, str):
            if clave.isalpha():  # Verifica si la clave contiene solo letras
                raise ValueError("La clave no puede contener solo letras.")
            elif set(clave).issubset(set(string.punctuation)):  # Verifica si la clave contiene solo caracteres especiales
                raise ValueError("La clave no puede contener solo caracteres especiales.")
            self.clave = self.obtener_valor_clave(clave)
        else:

            raise ValueError("La clave debe ser un número entero o una cadena de letras.")
        if len(str(clave)) < 4:
            raise MinimunCharacters

            raise TypeError("La clave debe ser un número entero o una cadena de caracteres.")


    def obtener_valor_clave(self, clave):
        # Convertir cada letra de la clave a su valor numérico y sumarlos
        return sum(ord(letra) for letra in clave)

    def encriptar(self, mensaje):
        if not mensaje or not mensaje.strip():
            raise EmptyMessage("No se puede encriptar un mensaje vacío.")
        
        mensaje_encriptado = ""
        for caracter in mensaje:
            mensaje_encriptado += chr(ord(caracter) + self.clave)
        return mensaje_encriptado

    def desencriptar(self, mensaje_encriptado):

        if not mensaje_encriptado or not mensaje_encriptado.strip():
            raise ValueError("El mensaje no ha sido encriptado previamente o está vacío.")

        try:
            mensaje_desencriptado = ""
            for caracter in mensaje_encriptado:
                mensaje_desencriptado += chr(ord(caracter) - self.clave)
            return mensaje_desencriptado
        except ValueError:
            raise ValueError("El mensaje encriptado está corrupto o ha sido modificado.")