# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
from MTO import MotorEncriptacion

# descediente de unittest.TestCase
class Test(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testNormal1(self):
        Entrance = "Hola Mundo"
        clave = 1234
        mi_motor = MotorEncriptacion(clave)
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
        clave = 14074
        mi_motor = MotorEncriptacion(clave)
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
        clave = 14074
        mi_motor = MotorEncriptacion(clave)
        "mensaje_encriptado = mi_motor.encriptar(Entrance)"
        # Cada metodo de prueba debe llamar un metodo assert
        # Proceso
        result = mi_motor.encriptar(Entrance)
        #Esperado
        expected = "㝧㜿㜧㝆㝦㝛㝧㝩㜧㝞㜻㝰㝃㝞"
        # para comprobar si la prueba pasa
        self.assertEqual(expected,result)

    def testExcepcion1(self):
        pass
    
    def testExcepcion2( self ):
        pass
    def testExcepcion3(self):
        pass


    def testError1( self ):
        pass

    def testError2( self ):
        pass
        
    def testError3( self ):
        pass

    def testError4( self ):
        pass

        






# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()
