# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
from MTO import MotorEncriptacion

# descediente de unittest.TestCase
class Test(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testNormal1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        pass

    def testNormal2(self):
        pass
    
    def testNormal3(self):
        pass



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