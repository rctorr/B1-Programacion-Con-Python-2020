from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Página de Inicio"
    return render_template('index.html', titulo = titulo)

@app.route('/acerca-de/')
def acerca_de():
    titulo = "Página de Acerca de Mi App"
    return "<h2>Esta es una página construida con Flask!</h2>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

