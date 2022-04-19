
## Tipos de dato

### OBJETIVO

- Usar los distintos tipos de datos deisponibles en Python
- Utiilizar funciones de cast para hacer conversiones de tipo

#### REQUISITOS

1. Python 3

#### DESARROLLO

Tipos de datos básicos en Python.

- Numéricos:   
    - int: Números enteros
    - float: Números con punto flotante
    - complex: Numeros complejos
    
- Texto:
    - string

- Booleanos:
    - True
    - False

La función `type()` retorna el tipo de dato de la variable que tenga como argumento.

Crear el programa `tipos_de_datos.py` para abordar los distintos tipos de datos en Python con el siguiente código, no es necesario que escribas todo el código ve agregando por bloques y ve ejecutando poco a poco, sigue las pautas de tu Instructor.

```
# Tipos de datos numéricos
entero = 4
print( "El dato introducido contiene:", entero )
print( "Es de tipo:", type(entero) )

pi = 3.14159
print("El dato introducido contiene:", pi)
print("Es de tipo:", type(pi) )

# Cadenas de texto
mensaje = "Hola Mundo"
print("El dato introducido contiene:", mensaje)
print("Es de tipo:", type(mensaje) )

# Datos booleanos
verdadero = True
print("El dato introducido contiene:", verdadero)
print("Es de tipo:", type(verdadero) )
```

La conversión de tipos de datos en Python se puede realizar con algunas de las siguientes funciones:

- `int()` Cambia a tipo entero.
- `float()` Cambia a tipo float.
- `str()` Cambia a tipo string.
- `bool()` Cambia a tipo bool.

También existe la función `input(mensaje)` que permite leer datos desde la entrada estándar (telcado) y guardar el resultado en una variable, es importante recordar que esta función siempre regresa valores de tipo cadena (str), así que si se requiere otro tipo de datos es necesario aplicar la conversión correspondiente.

Crear el programa `conversion_de_datos.py` para realizar conversión (cast) del tipo de dato de una variable, de igual forma ver escribiendo por bloques y ejecuando poco a poco para ir comparando los resultados.

```
# Se puede definir números como cadenas si se encierran en comillas
numero1 = "100"
numero2 = "3.14159"
print( type(numero1), type(numero1) )

# Para convertir a entero 
entero = int(numero1)
print( type(entero) )

# Para convertir a flotante
flotante = float(numero2)
print( type(flotante) )

# También se puede convertir un número a cadena de texto
num = 300
cadena = str(num)
print(type(cadena))

# Leyendo una cadena
nombre = inptu("Dame tu nombre: ")
print( nombre, type(nombre) )

# Leyendo un entero
edad = input("Dame tu edad: ")
print( edad, type(edad) )
```

¿Cómo hacemos para tener una variable de `edad` que sea de tipo `int`?
