# p08-model-template-nilai.py

from flask import Flask, render_template
from models import modelBerita

app = Flask(__name__)

content = "Virus Corono telah mewabah di dunia. Jaga kesehatan anda!"

@app.route('/')
def home():
	modelku = modelBerita()

	modelku.setJudul('Berita Terkini')
	modelku.setTanggal('02/03/2020')
	modelku.setIsi(content)
	
	return render_template("berita.html",judul=modelku.cetakJudul(),tanggal=modelku.cetakTanggal(), isi=modelku.cetakIsi())