from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pichi159'
app.config['MYSQL_DB'] = 'cadimss'

conexion = MySQL(app)

@app.route('/')

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/eci')
def url_eci():
    return render_template('eci.html')

@app.route('/pp')
def url_pp():
    return render_template('personales.html')

@app.route('/quirugico')
def url_quiru():
    return render_template('quirurgico.html')

@app.route('/trauma')
def url_trauma():
    return render_template('traumatismo.html')

@app.route('/transfusion')
def url_trans():
    return render_template('transfusion.html')

@app.route('/alegia')
def url_aler():
    return render_template('alergia.html')

@app.route('/adiccion')
def url_adic():
    return render_template('adiccion.html')

if __name__ =='__main__':
    app.run(debug=True, port=5000)