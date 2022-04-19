
## Cadenas de texto y format

### OBJETIVO

- Usar cadenas de texto
- Realizar operaciones con cadenas de texto
- Introducir argumento dentro de cadenas de texto usando format

#### REQUISITOS
 
1. Python 3

#### DESARROLLO

Las cadenas de texto son un tipo en Python que nos permite manipular texto, el cual puede ser de tamaño indeterminado.

Las cadenas pueden usar los operadores + (concatenar cadenas) y * (Concatena la misma cadena múltiples veces), vamos a nuestra ventana del Intérprete de Python y ejecutemos línea a línea el siguiente código:


```
# Creando una variable de tipo string o cadena de texto
d = "Hola mundo"                                                

# Podemos imprimir su contenido escribiendo sólo el nombre de la variable
d
'Hola mundo'

# Podemos comprobar el tipo de dato con type()
type(d)
str

# Podemos utilizar comillas simples, o tres comillas dobles
e = 'Saludos'
f = """
-------------------------------------------
What's your name?
"""

# Las cadenas pueden tener unicamente 1 caracter, o incluso 0
un_caracter = 'a'
un_caracter
'a'

cadena_vacia = ''
cadena_vacia
''
type(cadena_vacia)
str

# Operaciones con cadenas
"Hola" * 5 #'* Repite la misma cadena n-veces'
'HolaHolaHolaHolaHola'

"Hola" + " Mundo" #'+ concatena cadenas'
'HolaMundo'
```

La función format nos permite introducir argumentos dentro de cadenas de texto y darle formato.

Crea el archivo `formato.py` con el siguiente código para comprender como se puede formatear bloques de texto:

```
# format() sirve para añadir variables dentro de una cadena durante la ejecución
nombre = "Luis"  
print("Hola, mi nombre es {}".format(nombre)) # 'Hola!, mi nombre es Luis'

# Incluso se pueden agregar variables que no son cadenas
edad = 28
print("Tengo {} años".format(edad))

# O se pueden agregar multiples datos
print("{} + {} = {}".format(4, 5, 4+5))  # 4 + 5 = 9
```

Otra forma de formatear texto en Python es por medio del uso de las **f-string** que nos permite dar formato de la siguiente manera:

```
# Añadir variables dentro de una cadena durante la ejecución
print( f"Hola, mi nombre es {nombre}" )

# Incluso se pueden agregar variables que no son cadenas
print( f"Tengo {edad} años" )

# O se pueden agregar multiples datos
print( f"{4} + {5} = {4+5}" )
```
