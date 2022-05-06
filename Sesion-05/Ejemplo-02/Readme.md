## Decoradores

### OBJETIVO

- Usar decoradores para incrementar funcionalidad de funciones con o sin argumentos

#### REQUISITOS

1. Python 3


#### DESARROLLO

Los decoradores son funciones que reciben otra función como parámetro y devuelve otra función. Se suelen usar para incrementar la funcionalidad de la función recibida.

Para aplicar un decorador sobre una función, se coloca `@decorador` en la linea que precede a la definición de la función.

Primero veamos que podemos crear variables de tipo `function`:

```
In [20]: def fulano():
    ...:     print("Fulano")
    ...:     

In [21]: fulano()
Fuylano

In [22]: fulano
Out[22]: <function __main__.fulano()>

In [23]: a = fulano

In [24]: type(a)
Out[24]: function

In [25]: a()
Fulano
```
Así que podemos usar funciones como argumentos de funciones también, entonces podemos crear una función `hola(función)` cuyo argumento es una función que podemos llamar dentro de la nueva función, veamos como:

```
In [26]: def hola(f):
    ...:     print("Hola")
    ...:     f()
    ...:     

In [27]: hola()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-19da9312f5d0> in <module>
----> 1 hola()

TypeError: hola() missing 1 required positional argument: 'f'

In [28]: hola(fulano)
Hola
Fulano
```
**Notas improtantes:**
1. La función `f()` no está definida en el contexto de la función `hola()`
2. La función `f()` existe en el contexto de `hola()` porque se pasa como argumento
3. El orden de ejecución si importa, en este caso primero se ejecuta la función `print()` y luego la función `f()` o deberíamos decir `fulano()`.
4. Nota que cuando se ejecuta `hola(fulano)` la función `fulano` no se ejecuta porque no se están incluyendo los paréntesis
5. La función `fulano()` se ejecuta en la segunda línea de código de la función `hola(f)`, sólo que en su conexto ahora se llama `f` y para ejecutarla sólo se agregan los paréntesis al nombre de la función, en este caso `f()` que es equivalente a ejecutar `fulano()`.

Ahora veamos el concepto de **funciones internas**, que se define como la capacidad de definir funciones dentro de otras funciones, por ejemplo:

```
In [29]: def hola(f):
    ...:     def primera():
    ...:         print("desde el avismo de Python")
    ...:     def segunda():
    ...:         print("Hola")
    ...:     segunda()
    ...:     f()
    ...:     primera()
    ...:     

In [30]: hola(fulano)
Hola
Fulano
desde el avismo de Python
```
**Notas:**
1. Las funciones `primera()` y `segunda()` no existen fuera del contexto de la función `hola()`.
2. Las funciones `primera()` y `segunda()` no existen hasta que la función `hola()` se ejecuta y se crean como cualquier otra variable.
3. El órden de ejecución no está definido por el órden de definición, si no por el órden de ejecución, en este caso la función interna `segunda()` se ejecuta antes que `primera()`.

Ahora veamos que sucede cuando una función regresa una función y no confundir con el resultado de ejecutar una función, veamos un ejemplo:

```
In [37]: def hola():
    ...:     return "Hola"
    ...:     

In [38]: def mengano(f):
    ...:     return f
    ...:     

In [39]: mengano(hola)
Out[39]: <function __main__.hola()>

In [40]: hola
Out[40]: <function __main__.hola()>

In [41]: a = mengano(hola)

In [42]: a
Out[42]: <function __main__.hola()>

In [43]: a()
Out[43]: 'Hola'
```
**Notas:**
1. Aquí lo importante es notar como la función `a()` representa a la función `f()` que está dentro del contexto de `mengano()`, así que si la función `mengano()` tuviera varias funciones internas definidas, se podría elegir una y regresarla para su ejecución.

Entonces si queremos complementar la función `fulano()` con acciones que se pueden ejecutar antes y después de su llamada, usaamos la composición de función más una función interna que nos permite regresar una función que se pueda ejecutar en lugar de la función original y que ahora llamamos `saludo_fulano()`:

```
In [55]: def fulano():
    ...:     print("Fulano")
    ...:     

In [56]: def saludo(f):
    ...:     def mensaje():
    ...:         print("Hola")
    ...:         f()
    ...:         print("desde el avismo de las funciones!")
    ...:     return mensaje
    ...:     

In [57]: saludo(fulano)
Out[57]: <function __main__.saludo.<locals>.mensaje()>

In [58]: saludo_fulano = saludo(fulano)

In [59]: saludo_fulano
Out[59]: <function __main__.saludo.<locals>.mensaje()>

In [60]: saludo_fulano()
Hola
Fulano
desde el avismo de las funciones!
```
**Notas:**
1. Notar que en ningún momento se está modificando la función `fulano()`.
2. Se ha renombrado la composición de funciones como una variable nueva `saludo_fulano` pero que sigue siendo una función.
3. En Python para simplificar el uso de la composición de función se creó el concepto de **decoradores** para ejecutar sólo `fulano()` en luigar de `saludo(fulano)`.

Apliquemos nuestro primer decorador a la función `mengano()` de la forma:

```
In [61]: @saludo
    ...: def mengano():
    ...:     print("Mengano")
    ...:     

In [62]: mengano
Out[62]: <function __main__.saludo.<locals>.mensaje()>

In [63]: saludo(mengano)
Out[63]: <function __main__.saludo.<locals>.mensaje()>

In [64]: mengano()
Hola
Mengano
desde el avismo de las funciones!
```

Que sucede si nuestra función base necesita de argumentos, por ejemplo ahora en lugar de usar `fulano()` o `mengano()` creamos la función `usuario(nombre)` y el decorador `saludo(f)` deberá de imprimir el saludo usando el argumento `nombre` de nuestra función base.

```
In [65]: def usuario(nombre):
    ...:     return nombre.upper()
    ...:     

In [66]: def saludo(f):
    ...:     def mensaje(nombre):
    ...:         return f"Hola {f(nombre)} desde el avismo de Python!"
    ...:     return mensaje
    ...:     

In [67]: @saludo
    ...: def usuario(nombre):
    ...:     return nombre
    ...:     

In [68]: usuario("Fulano")
Out[68]: 'Hola FULANO desde el avismo de Python!'

In [69]: usuario("Mengano")
Out[69]: 'Hola MENGANO desde el avismo de Python!'

In [70]: usuario("Rctorr")
Out[70]: 'Hola RCTORR desde el avismo de Python!'

In [71]: usuario
Out[71]: <function __main__.saludo.<locals>.mensaje(nombre)>

In [72]: 
```
**Notas:**
1. Los parámetros que se pasan a la función `usuario` en realidad se le están pasando a la función interna `mensaje()`

Finalmente revisa los script `tiempo.py` y `numeros.py`, realiza los cambios necesarios para que obtengas un resultado similar al siguiente:

```
$ python numeros.py 10
0
1
2
3
4
5
6
7
8
9

Segundos totales de ejecución: 3.600120544433594e-05 seg
```

**Referencias:**
- [PEP 318 -- Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)