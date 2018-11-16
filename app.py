from flask import Flask, request, url_for, render_template
app = Flask(__name__)

"""@app.route('/')
def hello_world():
    return '<h1>Hola Mundo!</h1>'

@app.route('/reporteChino')
def reporte_chino():
    return '<h1>Reporte Chino</h1>'

@app.route('/cosaLoca/<id>')
def cosa_loca(id):
    return '<h1>Cosa Loca con id:{}</h1>'.format(id)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)"""

@app.route('/',methods=["GET", "POST"])
def inicio():
    return render_template("inicio.html", titulo="Ejemplo de aplicacion Flask")

@app.route('/suma', methods=["GET", "POST"])
def suma():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        try:
            resultado="Resultado de la suma:{}".format(str(int(num1)+int(num2)))
        except:
            resultado="No se puede realizar la suma"
        return  render_template("resultado.html", titulo="Resultado de la suma", resultado=resultado)
    else:
        return render_template("suma.html", titulo="Sumar")

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Pagine ne encontrade...</h1>', 404

if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug=True)