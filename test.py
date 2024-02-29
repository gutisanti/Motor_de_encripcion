# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import MTO

from MTO import MotorEncriptacion


# descediente de unittest.TestCase
class Test(unittest.TestCase):
    # Casos de prueba de encriptacion
    # Cada prueba unitaria es un metodo la clase
    def testNormal1(self):
        Entrance = "Hola Mundo"
        Key = 1234
        mi_motor = MTO.MotorEncriptacion(Key)
        "encrypted_message = mi_motor.encriptar(Entrance)"
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
        "encrypted_message = mi_motor.encriptar(Entrance)"
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
        "encrypted_message = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.encriptar(Entrance)
        #Esperado
        expected = "㜮㜬㜪"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    def testEmptyMessage(self):
        Entrance = ""
        clave = 14074
        mi_motor = MTO.MotorEncriptacion(clave)
        
        self.assertRaises(MTO.EmptyMessage, mi_motor.encriptar, Entrance)
    
    def testEmojiMessage( self ):
        # Mensaje con emojis
        Entrance = "😊😊😊😊"
        Key = 1234

        # Crear el motor de encriptación
        mi_motor = MTO.MotorEncriptacion(Key)

        # Proceso de encriptación
        encrypted_message = mi_motor.encriptar(Entrance)

        # Proceso de desencriptación
        mensaje_desencriptado = mi_motor.desencriptar(encrypted_message)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(mensaje_desencriptado, Entrance)

        
    def testMessageSinograms(self):
        # Mensajes para probar
        Entrance = "汉字"
        
        # Verifica si hay sinogramas en los mensajes
        self.assertTrue(MTO.has_sinogram(Entrance))

    def testMinimunCharacterKey(self):
        # Mensaje a encriptar
        entrance = "Hi bae"
        
        # Clave con menos de 4 caracteres
        clave = "140"  # Esta clave tiene solo 3 caracteres
        
        testOk = False
        try:
        # Crear el motor de encriptación
            mi_motor = MTO.MotorEncriptacion(clave)
        except MTO.MinimunCharacters :
            testOk = True
        self.assertTrue(testOk, "No se disparo lo esperado")



    def testModifiedEncryptedMessage(self):
        # Mensaje encriptado modificado
        encrypted_message = "ԂԃԄԃԂ"
        # Cambia un carácter del mensaje encriptado
        modified_encrypted_message = list(encrypted_message)
        # Por ejemplo, cambia el primer carácter de "Ԃ" a "ԃ"
        modified_encrypted_message[0] = "j"
        modified_encrypted_message = "".join(modified_encrypted_message)

        # Key y motor de encriptación
        Key = 1232
        mi_motor = MTO.MotorEncriptacion(Key)

        # Proceso de desencriptación
        try:
            result = mi_motor.desencriptar(modified_encrypted_message)
        except ValueError as e:
            # Se espera que se lance una excepción ValueError
            self.assertIsInstance(e, ValueError)
            # Verificar que el mensaje de la excepción sea el esperado
            self.assertEqual(str(e), "El mensaje encriptado está corrupto o ha sido modificado.")
        else:
            self.fail("Se esperaba que se lanzara una excepción ValueError pero no se lanzó.")
    

    def testKeyWithLetters( self):# Mensaje original
        # Mensaje original
        Entrance = "Hello World"

        # Key con solo letras
        Key = "abcd"

        # Intentar crear el motor de encriptación debería generar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor = MTO.MotorEncriptacion(Key)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "La clave no puede contener solo letras."
        self.assertEqual(expected_error_message, str(context.exception))

        
        
    def testKeyWithSpaces(self):
    # Clave con espacios
        clave_con_espacios = "12 34 56"

        # Intentar crear el motor de encriptación con una clave que contiene espacios debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor = MTO.MotorEncriptacion(clave_con_espacios)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "La clave no puede contener espacios."
        self.assertEqual(expected_error_message, str(context.exception))

    pass
   
    def testKeyWithSpecialCharacters( self ):
        # Mensaje original
        Entrance = "Hello World"

        # Key con solo caracteres especiales
        Key = "!@#$"

        # Intentar crear el motor de encriptación debería generar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor = MTO.MotorEncriptacion(Key)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "La clave no puede contener solo caracteres especiales."
        self.assertEqual(expected_error_message, str(context.exception))

        # Asegurarse de que la prueba general también pase
        self.assertTrue(True)

        

    #Casos de prueba de Desencripción
    
    def testCurrentKey(self):
        Entrance = "ԚՁԾԳӲԟՇՀԶՁ"
        Key = 1234
        mi_motor = MTO.MotorEncriptacion(Key)
        "encrypted_message = mi_motor.encriptar(Entrance)"

        result = mi_motor.desencriptar(Entrance)
        #Esperado
        expected = "Hola Mundo"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    def testMessageNumber(self):
        Entrance = "ԂԃԄԃԂ"
        Key = 1232
        mi_motor = MTO.MotorEncriptacion(Key)
        "encrypted_message = mi_motor.encriptar(Entrance)"
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
        "encrypted_message = mi_motor.encriptar(Entrance)"
       
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

        # Key y motor de encriptación
        Key = 1232
        mi_motor = MTO.MotorEncriptacion(Key)

        # Proceso de desencriptación
        try:
            result = mi_motor.desencriptar(modified_encrypted_message)
        except ValueError as e:
            # Se espera que se lance una excepción ValueError
            self.assertIsInstance(e, ValueError)
            # Verificar que el mensaje de la excepción sea el esperado
            self.assertEqual(str(e), "El mensaje encriptado está corrupto o ha sido modificado.")
        else:
            self.fail("Se esperaba que se lanzara una excepción ValueError pero no se lanzó.")

    #DESENCRIPTAR#
    
    def test_EmptyMessage( self ):
        # Mensaje encriptado vacío
        encrypted_message = ""

        # Key arbitraria
        key = 9876

        # Crear el motor de encriptación
        mi_motor = MTO.MotorEncriptacion(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(encrypted_message)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "El mensaje no ha sido encriptado previamente o está vacío."
        self.assertEqual(expected_error_message, str(context.exception))
        
    def testNoneMessage(self):
        # Valor None
        Entrance = None
        Key = 14074
        mi_motor = MTO.MotorEncriptacion(Key)
        
        # Intentar encriptar el valor None debería lanzar la excepción EmptyMessage
        with self.assertRaises(MTO.EmptyMessage):
            mi_motor.encriptar(Entrance)


    def testIncorectKey(self):
        # Clave correcta
        Key = 1234

        # Crear el motor de encriptación con la clave correcta
        mi_motor = MTO.MotorEncriptacion(Key)

        # Clave incorrecta
        clave_incorrecta = 5678

        # Intentar desencriptar con una clave incorrecta debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar("MensajeEncriptado", clave_incorrecta)

        # Verificar que el mensaje de error esperado está exactamente igual al mensaje de error real
        expected_error_message = "La clave proporcionada no coincide con la clave utilizada para encriptar el mensaje."
        self.assertEqual(expected_error_message, str(context.exception))




    def testUnencryptedmessage( self ):

        # Mensaje no encriptado
        mensaje_no_encriptado = "Hola Mundo"

        # Clave válida
        clave = 1234

        # Crear el motor y desencriptar un mensaje no encriptado debería lanzar una excepción
        mi_motor = MTO.MotorEncriptacion(clave)

        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(mensaje_no_encriptado)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "El mensaje encriptado está corrupto o ha sido modificado."
        self.assertEqual(expected_error_message, str(context.exception))
            
        
        
    def testCorruptMessage( self ):
        # Mensaje encriptado corrupto o modificado
        encrypted_message = "MensajeModificado"

        # Clave válida
        Key = 1234

        # Crear el motor y desencriptar el mensaje corrupto debería lanzar una excepción
        mi_motor = MTO.MotorEncriptacion(Key)

        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(encrypted_message)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "El mensaje encriptado está corrupto o ha sido modificado."
        self.assertEqual(expected_error_message, str(context.exception))
       

    def testEmptyKey( self ):
        # Mensaje encriptado vacío
        encrypted_message = ""

        # Key arbitraria
        key = 9876

        # Crear el motor de encriptación
        mi_motor = MTO.MotorEncriptacion(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(encrypted_message)

        # Verificar que la excepción tiene el mensaje esperado
        expected_error_message = "El mensaje no ha sido encriptado previamente o está vacío."
        self.assertEqual(expected_error_message, str(context.exception))
        pass
        # Mensaje original esperado (debería ser vacío)
        expected = ""
        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(expected, encrypted_message)
        


        
# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()
