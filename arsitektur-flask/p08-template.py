# file:p08.template.py
#contoh app Flask dengan template

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')