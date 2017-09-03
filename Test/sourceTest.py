import unittest
from Code.sourceCode import Programa3

class TestsPrograma3(unittest.TestCase):
	prg3=Programa3()

	def testAleatorios(self):
		self.prg3.generarAleatorios(100,200,5)
		self.assertEqual(len(self.prg3.x),5)

	def testSumXiYi(self):
		self.prg3.SumXiYi()
		self.assertNotEqual(self.prg3.sumXiYi,0)

	def testMedias(self):
		self.prg3.calcularMedias()
		self.assertNotEqual(self.prg3.xMedia,0)

	def testSumXiCuadrada(self):
		self.prg3.SumXiCuadrada()
		self.assertNotEqual(self.prg3.sumXiCuadrada,0)

	def testCalcularB1(self):
		self.prg3.CalcularB1()
		self.assertNotEqual(self.prg3.B1,0)

	def testCalcularCoeficiente(self):
		self.prg3.CalcularCoeficiente()
		self.assertNotEqual(self.prg3.r,0)

	def testCalcularPrediccion(self):
		self.prg3.CalcularPrediccion(210)
		self.assertNotEqual(self.prg3.yk,0)
		
	
if __name__ == '__main__':
	unittest.main()