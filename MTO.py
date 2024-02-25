class MotorEncriptacion:
    def __init__(self, clave):
        self.clave = clave

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
