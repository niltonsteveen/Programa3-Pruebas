import os
from flask import Flask, request, render_template
from Code.sourceCode import Programa3

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("template.html")

@app.route('/calcular' , methods=['POST'])
def calcular():
	if request.method == 'POST':
		n = request.form['n']
		xk = request.form['xk']
		minn = request.form['min']
		maxx = request.form['max']
		numeros=[]
		for i in range(0,int(n)):
			numeros.append(i)
		prg3 = Programa3()
		prg3.CalcularPrediccion(xk, minn, maxx, n)	
		return render_template("template.html",r=prg3.r, xk=xk, x=prg3.x, y=prg3.y, xcuadrada=prg3.x2, ycuadrada=prg3.y2, xy=prg3.xy, prediccion=prg3.yk, xmedia=prg3.xMedia, ymedia=prg3.yMedia, sumx2=prg3.sumXiCuadrada, sumy2=prg3.sumYiCuadrada, sumxy=prg3.sumXiYi, b0=prg3.B0, b1=prg3.B1, numeros=numeros, sumXi=prg3.sumXi, sumYi=prg3.sumYi)

if __name__ == '__main__':
	app.run()