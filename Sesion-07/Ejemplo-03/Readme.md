
## Formularios

### OBJETIVO

- Crear páginas con formularios usando Flask

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

Cuando una página contiene un formulario, éste se muestra como cualquier otra página y se usa el método o acción de tipo `GET`, éste es el método que usa un navegador cuando cuando solicita cualquier página, mientras no se indique un método diferente.

Entonces, nuevamente, la página de un formulario se solicita usando el método `GET` y en el navegador aparecerán los campos a llenar y generalmente un botón.

Cuando uno termina de llenar un formulario uno preciona normalmente el botón de **Enviar** entonces el navegador genera una petición al servidor, pero esta vez incluye los datos capturados y además el método ahora es **POST**.

En Flask para indicar que métodos son permitidos por una ruta, se realiza con el decorador `route()` como se muestra en el código más adelante.

Adicionalmente se tiene que hacer uso de un objeto de Flask llamado `request` (petición) que es una variable que almacena los datos capturador por el formulario, el método usado y otras muchas variables más, pero usando esta variable para obtener los datos del formulario se realiza con:

`request.form["name del campo"]`

Entonces es necesario agregar una nueva ruta y función a nuestra `mi-app.py` para que pueda atender las peticiones de la página de Contacto, notar que también se necesita del archivo `templates/contacto.html` que contiene el código HTML correspondiente.


```
@app.route('/contacto/', methods = ['GET', 'POST'])
def contacto():
    titulo = "Página de Contacto"
    if request.method == 'POST':
        nombre = request.form["nombre"]
        email = request.form["email"]
        comentarios = request.form["comentarios"]
        
        print("Los datos recibidos del formulario son:")
        print(f"Nombre: {nombre}")
        print(f"E-mail: {email}")
        print(f"Comentarios: {comentarios}")
        return index()

    return render_template('contacto.html', titulo = titulo)
```
