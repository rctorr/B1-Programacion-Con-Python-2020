## Pytest básicos

### OBJETIVO

- Realizar tests unitarios usando Pytest
- Ejecutar Pytest desde la terminal

#### REQUISITOS

1. Python 3
2. Pytest

#### DESARROLLO

Pytest es un paquete que nos permite automatizar pruebas unitarias de software escrito en Python.

Si no tienes instalado Pytest, puedes instalarlo usando `pip`:

```
programacion-con-python) rctorr@gatem:~$ pip install pytest
Collecting pytest
  Downloading pytest-7.1.2-py3-none-any.whl (297 kB)
     |████████████████████████████████| 297 kB 792 kB/s 
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting tomli>=1.0.0
  Downloading tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting iniconfig
  Downloading iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Collecting packaging
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 594 kB/s 
Collecting attrs>=19.2.0
  Downloading attrs-21.4.0-py2.py3-none-any.whl (60 kB)
     |████████████████████████████████| 60 kB 804 kB/s 
Collecting py>=1.8.2
  Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
     |████████████████████████████████| 98 kB 811 kB/s 
Collecting pyparsing!=3.0.5,>=2.0.2
  Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)
     |████████████████████████████████| 98 kB 813 kB/s 
Installing collected packages: pyparsing, tomli, py, pluggy, packaging, iniconfig, attrs, pytest
Successfully installed attrs-21.4.0 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.9 pytest-7.1.2 tomli-2.0.1
(programacion-con-python) rctorr@gatem:~$ 
```

Al utilizar Pytest, se suelen utilizar sentencias `assert`, este tipo de sentencias se evaluan, en caso de resultar True la ejecución de un programa continua, en caso contrario se lanza una señal de error.

Para realizar nuestro primer ejercicio de Pytest, vamos a evaluar si las funciones del módulo `operaciones.py` se ejecutan sin errores, las funciones a considerar son:

```
def suma(a, b=0):
    """ Calcula y regresa la suma de a con b """
    return a + b

def resta(a, b):
    """ Calcula y regresa la resta de a con b """
    return a + b

def producto(a, b=1):
    """ Calcula y regresa el producto de a con b """
    return a * b
```

Para usar pytest creamos un archivo cuyo nombre comienza por test, por ejemplo `test_operaciones.py`. En el cual importamos el módulo con las funciones a probar.

En este archivo se crean las funciones con nombre iniciando con test también, por ejemplo `test_funcion()`, en estas podemos incluir sentencias `assert` que llamen a la función a probar y las podemos comparar con el valor esperado.

```
import operaciones

def test_suma():
    assert operaciones.suma(2, 3) == 5
    assert operaciones.suma(2) == 2

def test_producto():
    assert operaciones.producto(3, 5) == 15
    assert operaciones.producto(2) == 2
```

Para ejecutar la prueba podemos dirigirnos en terminal a la carpeta contenedora de nuestro proyecto y ejecutamos

```console
(pcp) rctorr@fibo:Sesion-08/Ejemplo-01 $ pytest test_operaciones.py 
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-01
collected 2 items                               

test_operaciones.py ..                    [100%]

=============== 2 passed in 0.01s ===============
(pcp) rctorr@fibo:Sesion-08/Ejemplo-01 $ 
```

En este caso las pruebas han pasado sin errores, en caso de que la función evaluada contenga errores, por ejemplo si agregamos una prueba para la función `resta()`:

```
def test_resta():
    assert operaciones.resta(3, 2) == 1
    assert operaciones.resta(5, 5) == 0
    assert operaciones.resta(5, 11) == -6
```

Podemos ver la siguiente salida:

```
Sesion-08/Ejemplo-01 $ pytest test_operaciones.py 
============== test session starts ==============
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /mint/home/rctorr/Cursos/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-01
collected 3 items                               

test_operaciones.py ..F                   [100%]

=================== FAILURES ====================
__________________ test_resta ___________________

    def test_resta():
>       assert operaciones.resta(3, 2) == 1
E       assert 5 == 1
E        +  where 5 = <function resta at 0x7fe14c5353f0>(3, 2)
E        +    where <function resta at 0x7fe14c5353f0> = operaciones.resta

test_operaciones.py:12: AssertionError
============ short test summary info ============
FAILED test_operaciones.py::test_resta - asser...
========== 1 failed, 2 passed in 0.03s ==========
Sesion-08/Ejemplo-01 $ 
```

De forma similar se debe tener cuidado al crear las funciones test, por que si existe algún error en ella por ejemplo:

```
def test_suma():
    assert operaciones.suma(2, 3) == 4
    assert operaciones.suma(2) == 2
```

También se provocará un error
