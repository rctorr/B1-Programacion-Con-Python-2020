## Tests sobre clases y sus métodos

### OBJETIVO

- Crear test para clases y métodos

#### REQUISITOS

1. Pytest
2. Python 3

#### DESARROLLO

Hasta el momento hemos visto ejemplos de test unicamente con funciones, pero cuando trabajamos usando el paradigma orientado a objetos también se puede realizar tests unitarios, en estos casos la unidad básica a testear son los métodos de clase y se realiza de una manera similar a cuando se pruebas funciones.

Por ejemplo, si tenemos la siguiente definición de clase en `estudiante.py`:
```
import json

class EstudianteDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self,nombre):
        for estudiante in self.__data['estudiantes']:
            if estudiante ['nombre'] == nombre:
                return estudiante
```

La cual tiene métodos para conectarse a una base de datos json de estudiantes y devolver datos, si tenemos el siguiente json de prueba

```
{
    "estudiantes": [
        {
            "id": 1,
            "nombre": "Mario",
            "resultado": "aprobado"
        },
        {
            "id": 2,
            "nombre": "Luigi",
            "resultado": "reprobado"
        }
    ]
}
```

Podemos crear el script `test_estudiante.py` para el método `get_data()`:

```
import estudiante

db = estudiante.EstudianteDB()
db.connect('data.json')

def test_datos_luigi():
    luigi = db.get_data('Luigi')
    assert luigi['id'] == 2
    assert luigi['nombre'] == 'Luigi'
    assert luigi['resultado'] == 'reprobado'

def test_datos_mario():
    mario = db.get_data('Mario')
    assert mario['id'] == 1
    assert mario['nombre'] == 'Mario'
    assert mario['resultado'] == 'aprobado'
```

Al ejecutar las pruebas observamos:

```
Sesion-08/Ejemplo-03 $ pytest 
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
collected 2 items                               

test_estudiante.py FF                     [100%]

=================== FAILURES ====================
_______________ test_datos_luigi ________________

    def test_datos_luigi():
        luigi = db.get_data('Luigi')
>       assert luigi['id'] == 2
E       TypeError: string indices must be integers

test_estudiante.py:8: TypeError
_______________ test_datos_mario ________________

    def test_datos_mario():
        mario = db.get_data('Mario')
>       assert mario['id'] == 1
E       TypeError: string indices must be integers

test_estudiante.py:14: TypeError
============ short test summary info ============
FAILED test_estudiante.py::test_datos_luigi - ...
FAILED test_estudiante.py::test_datos_mario - ...
=============== 2 failed in 0.03s ===============
Sesion-08/Ejemplo-03 $ 
```

Que indica que ambas pruebas no han pasado, así que entonces hay que revisar nuestro código, corregirlo y ejecutar nuevamente las pruebas, éste proceso se repite hasta que todas las pruebas pasen, entonces podemos entregar nuestro código.

```
Sesion-08/Ejemplo-03 $ pytest 
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
collected 2 items                               

test_estudiante.py ..                     [100%]

=============== 2 passed in 0.01s ===============
Sesion-08/Ejemplo-03 $ 
```
