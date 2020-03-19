from flask import Flask, render_template
from models import lab_model

app=Flask(__name__)

data_lab = [
            {
                "nama": "Laboratorium 1",
                "spec": "Intel Core i3(3rd Gen), RAM 4GB, 500GB HDD, Monitor 19 inch",
                "jmlh": "45 PC"
            },
            {
                "nama": "Laboratorium 2",
                "spec": "Intel Core i5, RAM 4GB, 1TB HDD, Monitor 21.5 inch, Webcam Support",
                "jmlh": "50 PC"
            },
            {
                "nama": "Laboratorium 3",
                "spec": "Intel Core i3(4th Gen), RAM 4GB, 500GB HDD, Monitor 19 inch",
                "jmlh": "45 PC"
            },
            {
                "nama": "Laboratorium 4",
                "spec": "Intel Core i5, RAM 4GB, 1TB HDD, Monitor 21.5 inch, Webcam Support",
                "jmlh": "42 PC"
            },            
            {
                "nama": "Laboratorium 5",
                "spec": "Intel Core i3(3.30 Ghz), RAM 4GB, 500GB HDD, Monitor 16 inch",
                "jmlh": "42 PC"
            }
]


@app.route('/')
def home():
    lab=lab_model()

    lab.setNama('Laboratorium 1')
    lab.setSpec('Intel Core i3, RAM 4GB, 500GB HDD, Monitor 19 inch')
    lab.setJmlh('45 PC')

    return render_template("home.html", nama=lab.cetakNama(),
                                        spec=lab.cetakSpec(),
                                        jmlh=lab.cetakJmlh())

if __name__ == "__main__":
    app.run(debug=True)