import random
import math

class Programa3(object):
	"""docstring for Programa3"""
	def __init__(self):
		self.x=None
		self.y=None
		self.x2=None
		self.y2=None
		self.xy=None
		self.sumXiYi=0
		self.xMedia=0
		self.yMedia=0
		self.sumXiCuadrada=0
		self.sumYiCuadrada=0
		self.B1=0
		self.B0=0
		self.r=0
		self.sumXi=0
		self.sumYi=0
		self.yk=0

	def generarAleatorios(self,min,max,n):
		self.x=[]
		self.y=[]
		for i in range(0,n):
			self.x.append(random.randrange(min,max))
			self.y.append(random.randrange(min,max))

	def SumXiYi(self):
		self.xy=[]
		for i in range(0,len(self.x)):
			valor=self.x[i]*self.y[i]
			self.xy.append(valor)
			self.sumXiYi=self.sumXiYi+valor		

	def calcularMedias(self):
		for i in range(0,len(self.x)):
			self.xMedia=self.xMedia+self.x[i]
			self.yMedia=self.yMedia+self.y[i]
		self.xMedia=self.xMedia/len(self.x)
		self.yMedia=self.yMedia/len(self.y)

	def SumXiCuadrada(self):
		self.x2=[]
		for i in range(0,len(self.x)):
			valor=math.pow(self.x[i],2)
			self.x2.append(valor)
			self.sumXiCuadrada=self.sumXiCuadrada+valor

	def SumYiCuadrada(self):
		self.y2=[]
		for i in range(0,len(self.y)):
			valor=math.pow(self.y[i],2)
			self.y2.append(valor)
			self.sumYiCuadrada=self.sumYiCuadrada+valor

	def SumXi(self):
		for i in range(0,len(self.x)):
			self.sumXi=self.sumXi+self.x[i]

	def SumYi(self):
		for i in range(0,len(self.y)):
			self.sumYi=self.sumYi+self.y[i]

	def CalcularB1(self):
		self.SumXiYi()
		self.calcularMedias()
		self.SumXiCuadrada()
		self.B1=((self.sumXiYi)-(len(self.x)*self.xMedia*self.yMedia))/((self.sumXiCuadrada)-(len(self.x)*math.pow(self.xMedia,2)))
		self.CalcularB0()

	def CalcularB0(self):
		self.B0=(self.yMedia)-(self.B1*self.xMedia)

	def CalcularCoeficiente(self):
		self.SumXiYi()
		self.calcularMedias()
		self.SumXiCuadrada()
		self.SumYiCuadrada()
		self.SumXi()
		self.SumYi()
		self.r=((len(self.x)*self.sumXiYi)-(self.sumXi*self.sumYi))/math.sqrt(((len(self.x)*self.sumXiCuadrada)-(math.pow(self.sumXi,2)))*((len(self.y)*self.sumYiCuadrada)-(math.pow(self.sumYi,2))))

	def CalcularPrediccion(self, xk, minn, maxx, n):
		self.generarAleatorios(int(minn),int(maxx),int(n))
		self.SumXiYi()
		self.calcularMedias()
		self.SumXiCuadrada()
		self.SumYiCuadrada()
		self.SumXi()
		self.SumYi()
		self.r=((len(self.x)*self.sumXiYi)-(self.sumXi*self.sumYi))/math.sqrt(((len(self.x)*self.sumXiCuadrada)-(math.pow(self.sumXi,2)))*((len(self.y)*self.sumYiCuadrada)-(math.pow(self.sumYi,2))))
		self.yk=self.B0+(self.B1*int(xk))