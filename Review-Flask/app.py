# file: home.py
# contoh halaman web dengan Flask

from flask import Flask, render_template

app = Flask(__name__)

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