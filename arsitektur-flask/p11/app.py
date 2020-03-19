from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #jinja2 and loop
    #list untuk elemen bertipe tuple
    navigasi = [
        ('/','Beranda'),
        ('/profil','Profil'),
        ('/produk','Produk'),
        ('/kontak','Kontak2')
    ]
    return render_template("index.html", navigasi=navigasi)

@app.route('/profil')
def profil():
    return "<h2>Profil<h2>"

@app.route('/produk')
def produk():
    return "<h2>Produk<h2>"

@app.route('/kontak')
def kontak():
    # return "<h2>Kontak<h2>"
    return render_template("contact.html")