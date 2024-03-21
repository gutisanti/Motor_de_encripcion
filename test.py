import unittest
import MTO

class TestMotorEncryption(unittest.TestCase):

    def test_encrypt_encrypt_decrypt (self):
        # Caso de prueba para encrypt y luego decrypt un mensaje
        entrance = "Hola Mundo"
        key = 1234
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de encriptación y desencriptación
        encrypted_message = my_engine.encrypt(entrance)
        decrypted_message = my_engine.decrypt(encrypted_message)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(entrance, decrypted_message)

    def test_encrypt_mensaje_vacio(self):
        # Caso de prueba para encrypt un mensaje vacío
        entrance = ""
        key = 5678
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de encriptación debería lanzar una excepción
        with self.assertRaises(MTO.EmptyMessage):
            my_engine.encrypt(entrance)

    def test_decrypt_mensaje_vacio(self):
        # Caso de prueba para decrypt un mensaje vacío
        entrance = ""
        key = 5678
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError):
            my_engine.decrypt(entrance)

    def test_emoji_message(self):
        # Caso de prueba para encrypt y decrypt un mensaje con emojis
        entrance = "😊😊😊😊"
        key = 1234
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de encriptación y desencriptación
        encrypted_message = my_engine.encrypt(entrance)
        decrypted_message = my_engine.decrypt(encrypted_message)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(entrance, decrypted_message)

    def test_message_sinograms(self):
        # Caso de prueba para verificar sinogramas en un mensaje
        entrance = "汉字"

        # Comprobar si hay sinogramas en el mensaje
        self.assertTrue(MTO.has_sinogram(entrance))

    def test_minimun_character_key(self):
        # Caso de prueba para una key con menos de 4 caracteres
        entrance = "Hi bae"
        key = "140"  # key con solo 3 caracteres

        # Proceso de creación del motor debería lanzar una excepción
        with self.assertRaises(MTO.MinimunCharacters) as context:
            my_engine = MTO.EncryptionEngine(key)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "La key debe contener 4 caracteres minimo")

    def test_modified_encrypted_message(self):
        # Caso de prueba para un mensaje encriptado modificado
        encrypted_message = "ԂԃԄԃԂ"
        # Cambia un carácter del mensaje encriptado
        encrypted_message_modified = list(encrypted_message)
        # Por ejemplo, cambia el primer carácter de "Ԃ" a "ԃ"
        encrypted_message_modified[0] = "j"
        encrypted_message_modified = "".join(encrypted_message_modified)

        # CLave y motor de encriptación
        key = 1232
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine.decrypt(encrypted_message_modified)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_key_with_letters(self):
        # Caso de prueba para una key con solo letras
        entrance = "Hello World"
        key = "abcd"

        # Proceso de creación del motor debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine = MTO.EncryptionEngine(key)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "La key no puede contener solo letras.")

    def test_key_with_spaces(self):
        # Caso de prueba para una key con espacios
        key_with_spaces = "12 34 56"

        # Proceso de creación del motor con key que contiene espacios debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine = MTO.EncryptionEngine(key_with_spaces)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "La key no puede contener espacios.")

    def test_key_with_special_characters(self):
        # Caso de prueba para una key con solo caracteres especiales
        entrance = "Hello World"
        key = "!@#$"

        # Proceso de creación del motor debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine = MTO.EncryptionEngine(key)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "La key no puede contener solo caracteres especiales.")

    def test_current_key(self):
        # Caso de prueba para una key actual
        encrypted_message = "ԚՁԾԳӲԟՇՀԶՁ"
        key = 1234
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación
        result = my_engine.decrypt(encrypted_message)

        # expected
        expected = "Hola Mundo"

        # Verificar que el result de la desencriptación sea igual al mensaje original
        self.assertEqual(expected, result)

    def test_message_number(self):
        # Caso de prueba para un mensaje con números
        encrypted_message = "ԂԃԄԃԂ"
        key = 1232
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación
        result = my_engine.decrypt(encrypted_message)

        # expected
        expected = "23432"

        # Verificar que el result de la desencriptación sea igual al mensaje original
        self.assertEqual(expected, result)

    def test_character_message(self):
        # Caso de prueba para un mensaje con caracteres especiales
        encrypted_message = "ਣਰ੕ਤਝવ"
        key = 2550
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación
        result = my_engine.decrypt(encrypted_message)

        # expected
        expected = "-:_.'¿"

        # Verificar que el result de la desencriptación sea igual al mensaje original
        self.assertEqual(expected, result)

    def test_modified_encrypted_message(self):
        # Caso de prueba para un mensaje encriptado modificado
        encrypted_message = "ԂԃԄԃԂ"
        # Cambia un carácter del mensaje encriptado
        encrypted_message_modified = list(encrypted_message)
        # Por ejemplo, cambia el primer carácter de "Ԃ" a "ԃ"
        encrypted_message_modified[0] = "j"
        encrypted_message_modified = "".join(encrypted_message_modified)

        # Key y motor de encriptación
        key = 1232
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine.decrypt(encrypted_message_modified)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_empty_message(self):
        # Caso de prueba para un mensaje vacío
        entrance = ""
        key = 14074
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de encriptación debería lanzar una excepción
        with self.assertRaises(MTO.EmptyMessage):
            my_engine.encrypt(entrance)

    def test_none_message(self):
        # Caso de prueba para un mensaje None
        entrance = None
        key = 14074
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de encriptación debería lanzar una excepción
        with self.assertRaises(MTO.EmptyMessage):
            my_engine.encrypt(entrance)

    def test_incorrect_key(self):
        # Caso de prueba para una clave incorrecta
        encrypted_message = "Mundial"
        correct_key = 1234
        incorrect_key = 5678
        my_engine = MTO.EncryptionEngine(correct_key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine.decrypt(encrypted_message, incorrect_key)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "La key proporcionada no coincide con la key utilizada para encrypt el mensaje.")

    def test_unencrypted_message(self):
        # Caso de prueba para un mensaje no encriptado
        unencrypted_message = "Hola Mundo"
        key = 1234
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine.decrypt(unencrypted_message)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_corrupt_message(self):
        # Caso de prueba para un mensaje encriptado corrupto
        corrupt_encrypted_message = "Biologia"
        key = 1234
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine.decrypt(corrupt_encrypted_message)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_empty_key(self):
        # Caso de prueba para una key vacía
        encrypted_message = ""
        key = 9876
        my_engine = MTO.EncryptionEngine(key)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            my_engine.decrypt(encrypted_message)

        # Verificar que la excepción tiene el mensaje expected
        self.assertEqual(str(context.exception), "El mensaje no ha sido encriptado previamente o está vacío.")


# Este fragmento de código permite ejecutar la prueba individualmente
if __name__ == '__main__':
    unittest.main()
