from flask import Flask

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
	    <a href="index.html">Inicio</a> |
	    <a href="acerca-de.html">Acerca de</a>
	</nav>
	<hr />
	<h1>Hola mundo, soy una aplicación creada en Flask</h1>
	<hr />
    </body>
</html>    
    """

if __name__ == "__main__":
    app.run(debug=True)