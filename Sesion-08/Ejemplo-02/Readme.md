## Test unitarios avanzados

### OBJETIVO

- Se crearan archivos con múltiples test para una misma función
- Se abordarán opciones al ejecutar tests.

#### REQUISITOS

1. Python 3
2. Pytest

#### DESARROLLO

Al crear tests unitarios se puede establecer condiciones dentro de los assert que no unicamente evaluan la igualdad de la salida de la función con un valor, de hecho dentro de los assert se puede colocar cualquier expresión que devuelva un valor booleano.

Por ejemplo, creamos nuevamente el script `test_operaciones.py` con la siguiente función que evalua el uso de la función suma con entradas de tipo str:

```
def test_suma_string():
    resultado = operaciones.suma('Hola ', 'Mundo')
    assert resultado == 'Hola Mundo'
    assert type(resultado) is str
    assert len(resultado) > 0
```

Si ejecutamos pytest sin ningún parametro buscará de forma automática los archivos con la forma `test_archivo.py` y en ellos, las funciones `test_funcion()`, así que el resultado deberá de ser similar a lo siguiente:

```console
Sesion-08/Ejemplo-02 $ pytest 
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02
collected 1 item                                

test_operaciones.py .                     [100%]

=============== 1 passed in 0.01s ===============
Sesion-08/Ejemplo-02 $ 
```

Si queremos obtener una mayor información, podemos usar la opción -v (verbose), mostrando el resultado individual para cada test:

```
Sesion-08/Ejemplo-02 $ pytest -v
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0 -- /home/rctorr/miniconda3/envs/pcp/bin/python
cachedir: .pytest_cache
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02
collected 1 item                                

test_operaciones.py::test_suma_string PASSED [100%]

=============== 1 passed in 0.01s ===============
Sesion-08/Ejemplo-02 $ 
```

Se puede seleccionar el archivo de test a ejecutar con la sintaxis vista en el ejemplo anterior, o bien seleccionar una función de test especifica.

```
Sesion-08/Ejemplo-02 $ pytest test_operaciones.py::test_suma_string
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02
collected 1 item                                

test_operaciones.py .                     [100%]

=============== 1 passed in 0.00s ===============
Sesion-08/Ejemplo-02 $ 
```
