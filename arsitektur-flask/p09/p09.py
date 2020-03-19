from flask import Flask, render_template
from models import lab_model

app=Flask(__name__)

@app.route('/')
def home():
    lab=lab_model()

    lab.setNama('Laboratorium 1')
    lab.setSpec('"Intel Core i3", "RAM 4GB", "500GB HDD", "Monitor 19 inch"')
    lab.setJmlh('45 PC')

    return render_template("home.html", nama=lab.cetakNama(),
                                        spec=lab.cetakSpec(),
                                        jmlh=lab.cetakJmlh())

if __name__ == "__main__":
    app.run(debug=True)