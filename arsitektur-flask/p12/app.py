import csv
from flask import Flask, abort, render_template

app = Flask(__name__)

def get_data():
    csv_path = './static./province.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    
    return csv_list

def get_death():
    csv_path = './la-riots-deaths.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)

    return csv_list

@app.route('/')
def index():
    object_list = get_data()

    return render_template("index.html",object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    object_list = get_data()
    for row in object_list:
        if row['province_id'] == row_id:
            return render_template("detail.html", object=row)
    abort(404)

@app.route('/la-death/')
def los_angeles():
    object_list = get_death()

    return render_template("death.html", object_list=object_list)

@app.route('/la-death/<row_id>')
def la_details(row_id):
    object_list = get_data()
    for row in object_list:
        if row['province_id'] == row_id:
            return render_template("detail.html", object=row)
    abort(404)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)