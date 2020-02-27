# file: angkatan.py

from flask import Flask

app = Flask(__name__)

@app.route('/angkatan/<int:tahun>')
def angkatan(tahun):
    if tahun == 2016:
        return "<h2>Angkatan 2016 </h2><p>Anda harus lulus tahun ini</p>"
    elif tahun == 2017:
        return "<h2>Angkatan 2017</h2><p>Bersiap menghadapi Tugas Akhir</p>"
    elif tahun == 2018:
        return "<h2>Angkatan 2018</h2><p>Tugas kuliah semakin banyak</p>"
    elif tahun == 2019:
        return "<h2>Angkatan 2019</h2><p>Selamat belajar dengan dosen baru</p>"
    else:
        return "<h2>Anda belum memilih angkatan</h2><ul><li>2016</li><li>2017</li><li>2018</li><li>2019</li></ul>"
