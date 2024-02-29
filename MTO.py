import string

class EmptyMessage(Exception):
    """No se puede encriptar un mensaje vacio"""
<<<<<<< HEAD
=======

class MessageSinograms(Exception):
    """No se pueden encriptar sinogramas"""

class MinimunCharacters():
    """La clave debe contener 4 caracteres minimo"""

class IncorrectKey():
    """La clave esta incorrecta"""

>>>>>>> 3acb493f93ff61519ee12da2646d571e4419d626
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
<<<<<<< HEAD

            raise ValueError("La clave debe ser un número entero o una cadena de letras.")
        if len(str(clave)) < 4:
            raise MinimunCharacters

            raise TypeError("La clave debe ser un número entero o una cadena de caracteres.")

=======
            raise TypeError("La clave debe ser un número entero o una cadena de caracteres.")


>>>>>>> 3acb493f93ff61519ee12da2646d571e4419d626

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
<<<<<<< HEAD
            raise ValueError("El mensaje encriptado está corrupto o ha sido modificado.")
=======
            raise ValueError("El mensaje encriptado está corrupto o ha sido modificado.")

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

    # Verifica si alguno de los caracteres del mensaje es un sinograma
    for caracter in mensaje:
        for start, end in sinogram_ranges:
            if ord(caracter) >= start and ord(caracter) <= end:
                return True
    return False
>>>>>>> 3acb493f93ff61519ee12da2646d571e4419d626
