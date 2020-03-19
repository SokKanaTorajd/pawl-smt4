from flask import Flask, render_template
from models import dataMhs

app = Flask(__name__)

@app.route('/')
def home():
    mhs=dataMhs()

    mhs.setNama('T Wijatama D')
    mhs.setNim('182103010')
    mhs.setProdi('S1 - Sistem Informasi')

    return render_template("mahasiswa.html",nama=mhs.cetakNama(),
                                            nim=mhs.cetakNim(),
                                            prodi=mhs.cetakProdi())
