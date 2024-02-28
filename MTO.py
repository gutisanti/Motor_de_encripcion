
class EmptyMessage(Exception):
    """No se puede encriptar un mensaje vacio"""
class MotorEncriptacion:
    def __init__(self, clave):

        if isinstance(clave, int):
            self.clave = clave
        elif isinstance(clave, str):
            self.clave = self.obtener_valor_clave(clave)
        else:
            raise ValueError("La clave debe ser un número entero o una cadena de letras.")


    def obtener_valor_clave(self, clave):
        # Convertir cada letra de la clave a su valor numérico y sumarlos
        return sum(ord(letra) for letra in clave)


    def encriptar(self, mensaje):
        mensaje_encriptado = ""
        for caracter in mensaje:
            mensaje_encriptado += chr(ord(caracter) + self.clave)
        return mensaje_encriptado

    def desencriptar(self, mensaje_encriptado):
        mensaje = ""
        for caracter_encriptado in mensaje_encriptado:
            mensaje += chr(ord(caracter_encriptado) - self.clave)
        return mensaje
