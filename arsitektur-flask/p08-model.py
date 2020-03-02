# p08-model.py
# contoh app routing dengan variable pada flask

from flask import Flask
from models import contohModel

app = Flask(__name__)

@app.route('/')
def home():
	# membuat objek dari kelas contohModel
	modelku = contohModel()

	#mengambil nilai dari model tsb
	return modelku.cetakTeks()