## Docstrings

### OBJETIVO

- Utilizar docstrings

#### REQUISITOS

1. Python 3

#### DESARROLLO

Cuando escribimos software es de utilidad dar una ayuda a quien podria consumirlos, para esto nos sirven los docstrings.

Los docstrings se generan entre comillas triples

Para agregar ayuda general en un paquete, se hace en el archivo __init__.py
```
""" Paquete de funciones sencillas """
```
Para agregarla en un modulo, se hace en la parte superior
Para funciones, debajo de su nombre
```
# Aplicaciones extras

def tabla(n):
    """ Imprime la tabla de multiplicar del numero introducido """
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n * i))
```

Modifica el archivo `helado.__init__.py` para agregar un texto de ayuda para todo el paquete, luego modifica el archivo `helado/varios.py` y agrega un texto de ayuda para todo el módulo.

En IPython importa el paquete y solicita su ayuda, luego importa el módulo `varios.py` y solicita su texto de ayuda, luego importa una función de cualquier módulo y solicita la ayuda de la función:

```
import helado


from helado import varios


from helado.pantalla import imprime_toppings

```

