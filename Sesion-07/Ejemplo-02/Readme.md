
## Rutas y parámetros

### OBJETIVO

- Crear páginas con múltiples rutas
- Incluir argumentos en las rutas

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

**PARÁMETROS**

Además de tener múltiples rutas es posible crear páginas que acepten argumentos por medio de la URL, por ejmplo:

- http://127.0.0.01:5000/hola/pluto/

Genera la página que dirá:

`Hola Pluto como estás!`

- http://127.0.0.01:5000/hola/rctorr/

Genera la página que dirá:

`Hola Rctorr como estás!`

Para eso al momento de crear una ruta se define una variable y el tipo de dato que uno espera, vamos a agregar el siguiente código a programa de `mi-app.py`

```
@app.route('/hola/<str:nombre>/')
def hola(nombre):
    return f"<h1>Hola {nombre} como estás!</h1>"
```
