## Paquetes

### OBJETIVO

- Crear paquetes
- Acceder a modulos y funciones que estan en paquetes

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los paquetes nos permiten reunir varios modulos dentro de una carpeta, para que python reconozca una carpeta como un modulo, es necesario que tenga un archivo con nombre `__init__.py` (incluso puede estar vacio)

Para acceder a los elementos de un paquete usamos import, de manera similar a un modulo, primero revisemos el contenido de la carpeta `helado/`

```
helado
├── entrada.py
├── __init__.py
├── pantalla.py
└── varios.py
```

Entonces como el archivo `__init__.py` existe esta carpeta se reconoce como un paquete en Python y los archivos `entrada.py`, `pantalla.py` y `varios.py` son los módulos de este paquete.

Ahora vamos a acceder a este paquete desde IPython:

```
In [11]: # Importando un módulo desde el paquete

In [12]: import helado.varios

In [13]: # Importando un módulo desde el paquete

In [14]: helado.varios.borrar_terminal()

In [15]: from helado import entrada

In [16]: r = entrada.lee_respuesta()
Elige el topping: 1

In [17]: r
Out[17]: 1

n [2]: # Importando sólo algunos elementos

In [3]: from helado.pantalla import imprime_toppings

In [4]: imprime_toppings?
Signature: imprime_toppings(menu)
Docstring: Imprime la lista de opciones de toppings 
File:      ~/Escritorio/TECP0006FSPYOL2102/Sesion-03/Ejemplo-04/helado/pantalla.py
Type:      function

In [5]: imprime_toppings(helado.varios.menu)

-------------------------
1. Helado con oreo
2. Helado con m&m
3. Helado con fresas
4. Helado con brownie
-------------------------
```

Ahora modifica el script `helado_precio.py` para que haga uso de los componentes del módulo para hacer que el programa nuevamente funcione como lo venía haciendo.

