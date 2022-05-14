from flask import Flask
from flask import render_template
from flask import request
import productos

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Productos Inicio"
    productos_lista = productos.lista_productos()
    return render_template("index.html", titulo=titulo, productos=productos_lista)
 
@app.route('/panel/')
def panel(msg=""):
    titulo = "Productos - Panel"
    return render_template("panel.html", titulo=titulo, msg=msg)

@app.route('/producto/alta/', methods=['GET', 'POST'])
def producto_alta():
    titulo = "Productos - Alta"
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        descripcion = request.form["descripcion"]
        productos.alta(nombre, precio, descripcion)
        # return para el método POST
        return panel(msg="El producto se dió de alta de forma correcta!")

    # return para el método GET
    return render_template("producto-alta.html", titulo=titulo)

@app.route('/productos/')
def productos_lista():
    pass

@app.route('/producto/modificar/<int:id_>/', methods=['GET', 'POST'])
def producto_modificar(id_):
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

