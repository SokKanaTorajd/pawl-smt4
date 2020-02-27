# file: app.py
# contoh halaman web dengan Flask

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "<h2>Halo</h2><p>Selamat datang di kelas Pengembangan Aplikasi Web dengan Flask</p>"

# @app.route('/profil')
# def profil():
#     return "<h2>Profil</h2><p>Aplikasi ini dibuat oleh <strong>Wijatama D</strong></p>"

# @app.route('/salam/<nama>')
# def salam(nama):
#     return "<h2>Selamat Datang!</h2><p>Selamat datang <strong>"+str(nama)+"</strong> di Aplikasi Flask</p>"

# @app.route('/umur/<int:usia>')
# def umur(usia):
#     return "<h2>Umur</h2><p>umurku anda adalah <strong>"+str(usia)+" tahun</strong></p>"

# @app.route('/pajak/<int:dana>')
# def pajak(dana):
#     hasil = (5/100) * dana
#     return "<h2>Hitung Pajak</h2><p>Pajak Penghasilan (PPh) dari Rp <strong>"+str(dana)+"</strong> adalah <strong>"+str(hasil)+"</strong></p>"

# @app.route('/semester/<periode>')
# def semester(periode):
#     if periode == "ganjil":
#         return "<h2>Semester Ganjil</h2><p>Kuliah dilaksanakan pada bulan September-Desember. UAS dilaksanakan pada bulan Januari</p>"
#     elif periode =="genap":
#         return "<h2>Semester Genap</h2><p>Kuliah dilaksanakan pada bulan Februari-Mei. UAS dilaksanakan pada bulan Juni</p>"
#     else:
#         return "<h2>Pilih Semester</h2><p>Anda belum memilih semester ('ganjil' atau 'genap')</p>"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profil/')
def about():
    return render_template('profil.html')

@app.route('/prodi/')
def major():
    return render_template('prodi.html')

@app.route('/kampus/')
def university():
    return render_template('kampus.html')

if __name__ == "__main__":
    app.run(debug=True)
