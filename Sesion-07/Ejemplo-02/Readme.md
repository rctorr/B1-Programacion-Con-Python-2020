
## Rutas y plantillas (templates)

### OBJETIVO

- Crear páginas con múltiples rutas
- Incluir argumentos en las rutas

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

**Plantillas (templates)**

Generar el código HTML de forma directa no es lo ideal, si no que hacemos uso del sistema de plantillas (templates) que proporcionan los distintos framewroks, en éste caso **Flask**, así que continuando con el caso del Ejemplo-01, vamos a hacer que la ruta `/acerca-de` muestre el contenido del archivo `public_html/acerca-de.html`, para ello tenemos que relacionar los siguientes tres componentes:

1. Ruta o url `/acerca-de`
2. Función encargada de procesar la vista: `acerca_de()`
3. Plantilla encargada de generar el HTML final: `templates/acerca-de.html`

Agreguemos el siguiente código al script `hola-flask.py`

```
@app.route('/acerca-de')
def acerca_de():
    return render_template('acerca-de.html')
```

Y copia el archivo `public_html/acerca-de.html` a la carpeta `templates`, tu archivos deberían de estar algo similar a lo siguiente:

```
Ejemplo-02
├── hola-flask.py
├── public_html
│   ├── acerca-de.html
│   └── index.html
├── Readme.md
└── templates
    ├── acerca-de.html
    └── readme.md
```

Finalmente actualiza el código HTML de la función `index()` para que las etiquetas `<a href="...">` apunten a las rutas, no a los archivos html.

Recuerda remplaza:

1. `index.html` por `/`
2. `acerca-de.html` por `/acerca-de`

También tienes que realizar el cambio en el archivo `templates/acerca-de.html`

Listo, ahora ya puedes navega entre las distintas páginas de tu primer aplicación web.
