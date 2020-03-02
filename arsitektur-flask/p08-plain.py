# file: p08.plain.py
# contoh app flask tanpa model dan template


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "<h2>Halo</h2><p>Selamat datang di kelas Pengembangan Aplikasi Web dengan Flask</p>"