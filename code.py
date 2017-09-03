import os
from flask import Flask, request, render_template

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("template.html")

if __name__ == '__main__':
	app.run()