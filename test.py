# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import MTO

# descediente de unittest.TestCase
class Test(unittest.TestCase):
    # Casos de prueba de encriptacion
    # Cada prueba unitaria es un metodo la clase
    def testNormal1(self):
        Entrance = "Hola Mundo"
        Key = 1234
        mi_motor = MTO.MotorEncriptacion(Key)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.encriptar(Entrance)
        #Esperado
        expected = "ԚՁԾԳӲԟՇՀԶՁ"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    def testNormal2(self):
        Entrance = "mE-Llamo-dAvId"
        Key = 14074
        mi_motor = MTO.MotorEncriptacion(Key)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.encriptar(Entrance)
        #Esperado
        expected = "㝧㜿㜧㝆㝦㝛㝧㝩㜧㝞㜻㝰㝃㝞"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    
    def testNormal3(self):
        Entrance = "420"
        Key = 14074
        mi_motor = MTO.MotorEncriptacion(Key)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.encriptar(Entrance)
        #Esperado
        expected = "㜮㜬㜪"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    def testEmptyMessage(self):
        Entrance = " "
        Key = 14074
        mi_motor = MTO.MotorEncriptacion(Key)
        
        try:
            result = mi_motor.encriptar(Entrance)
            self.assertEqual(result," ")
        
        except MTO.EmptyMessage:
            print("Expeción Ocurrida")

        # para comprobar si la prueba pasa
        
    
    def testEmojiMessage( self ):
         # Mensaje con emojis
        Entrance = "😊😊😊😊"
        Key = 1234

        # Crear el motor de encriptación
        mi_motor = MTO.MotorEncriptacion(Key)

        # Proceso de encriptación
        mensaje_encriptado = mi_motor.encriptar(Entrance)

        # Proceso de desencriptación
        mensaje_desencriptado = mi_motor.desencriptar(mensaje_encriptado)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(mensaje_desencriptado, Entrance)

        pass
    def testMessageSinograms(self):
        pass


    def MinimunCharacterKey( self ):
        pass

    def testKeyWithLetters( self):# Mensaje original
        Entrance = "Hola Mundo"
        
        # Clave con letras
        Key = "Hardkey"

        # Crear el motor de encriptación
        mi_motor = MTO.MotorEncriptacion(Key)

        # Proceso de encriptación
        mensaje_encriptado = mi_motor.encriptar(Entrance)

        # Proceso de desencriptación
        mensaje_desencriptado = mi_motor.desencriptar(mensaje_encriptado)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(mensaje_desencriptado, Entrance)

        pass
        
    def KeyWithSpaces( self ):
        pass

    def KeyWithCharacters( self ):
        pass

    #Casos de prueba de Desencripción
    
    def testCurrentKey(self):
        Entrance = "ԚՁԾԳӲԟՇՀԶՁ"
        Key = 1234
        mi_motor = MTO.MotorEncriptacion(Key)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"

        result = mi_motor.desencriptar(Entrance)
        #Esperado
        expected = "Hola Mundo"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    def testMessageNumber(self):
        Entrance = "ԂԃԄԃԂ"
        Key = 1232
        mi_motor = MTO.MotorEncriptacion(Key)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.desencriptar(Entrance)
        #Esperado
        expected = "23432"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    
    def testCharacterMessage(self):
        Entrance = "ਣਰ੕ਤਝવ"
        Key = 2550
        mi_motor = MTO.MotorEncriptacion(Key)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.desencriptar(Entrance)
        #Esperado
        expected = "-:_.'¿"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

def testModifiedEncryptedMessage(self):
    # Mensaje encriptado modificado
    encrypted_message = "ԂԃԄԃԂ"
    # Cambia un carácter del mensaje encriptado
    modified_encrypted_message = list(encrypted_message)
    # Por ejemplo, cambia el primer carácter de "Ԃ" a "ԃ"
    modified_encrypted_message[0] = "j"
    modified_encrypted_message = "".join(modified_encrypted_message)

    # Clave y motor de encriptación
    Key = 1232
    mi_motor = MTO.MotorEncriptacion(Key)

    # Proceso de desencriptación
    result = mi_motor.desencriptar(modified_encrypted_message)

    # Comprobación
    # Se espera que la desencriptación falle o produzca un resultado diferente
    self.assertNotEqual("23432", result)
   
    def testEmptyMessage( self ):
        pass
    def NoneMessage(self):
        pass


    def testIncorectKey( self ):
        pass

    def testUnencryptedmessage( self ):
        pass
        
    def testCorruptMessage( self ):
        pass

    def testEmptyKey( self ):
        pass

        






# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()
