from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
    <head>
	<meta charset="utf-8" />
    </head>
    <body>
        <nav>
	    <a href="/">Inicio</a> |
	    <a href="/acerca-de">Acerca de</a>
	</nav>
	<hr />
	<h1>Hola mundo, soy una aplicación creada en Flask</h1>
	<hr />
    </body>
</html>    
    """

@app.route('/acerca-de')
def acerca_de():
    return render_template('acerca-de.html')

@app.route('/saludos')
def saludos():
    nombre_get = request.args.get('nombre', 'Humano')
    nombre_get = nombre_get.title()
    return render_template("saludos.html", nombre=nombre_get)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")