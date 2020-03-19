from flask import Flask, render_template
from models import Lingkaran

app = Flask(__name__)

@app.route('/')
def index():
    str_var = 'Pengembangan Aplikasi Web lanjut'
    int_var = 20
    float_var = 24.1