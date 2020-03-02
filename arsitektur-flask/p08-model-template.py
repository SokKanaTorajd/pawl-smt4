#contoh app Flask dengan & model template

from flask import Flask, render_template
from models import contohModel

app = Flask(__name__)

@app.route('/')
def home():
	modelku = contohModel()

	return render_template("halo.html",modelku=modelku)



	# set FLASK_APP=<nama program python>
	# localhost:5000/