## Manipulación de archivos

### OBJETIVO

- Crear archivos de texto nuevos
- Leer archivos de texto
- Escribir archivos de texto
- Usar with en archivos

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los archivos en Python son objetos tipo *file* creados mediante la función *open* (abrir). Toma como parámetros una cadena con la ruta, y 2 opcionales, modo de acceso y tamaño de búfer.

```
In [1]: # Creando y escribiendo archivos de texto plano en Python

In [2]: archivo_txt = open("hola.txt", "w")

In [3]: archivo_txt.write("Hola archivos desde Python")
Out[3]: 26

In [4]: archivo_txt.close()

In [5]: archivo_txt = open("hola.txt", "a")

In [6]: archivo_txt.write("Hola2 desde Python")
Out[6]: 18

In [7]: archivo_txt.close()




In [8]: archivo_txt = open("hola.txt", "a")

In [9]: archivo_txt.write("\nHola2 desde Python\n")
Out[9]: 20

In [10]: archivo_txt.close()

In [11]: archivo_txt = open("hola.txt", "a")

In [12]: archivo_txt.write("Hola3 desde Python\n")
Out[12]: 19

In [13]: archivo_txt.write("Hola4 desde Python\n")
Out[13]: 19

In [14]: archivo_txt.close()



In [15]: archivo_txt = open("hola.txt", "r")

In [16]: type(archivo_txt)
Out[16]: _io.TextIOWrapper

In [17]: texto = archivo_txt.read()

In [18]: texto
Out[18]: 'Hola archivos desde Python\nHola2 desde Python\nHola3 desde Python\nHola4 desde Python\n'

In [19]: print(texto)
Hola archivos desde Python
Hola2 desde Python
Hola3 desde Python
Hola4 desde Python


In [20]: texto.split("\n")
Out[20]: 
['Hola archivos desde Python',
 'Hola2 desde Python',
 'Hola3 desde Python',
 'Hola4 desde Python',
 '']

In [21]: archivo_txt.close()


In [22]: archivo_txt = open("hola.txt", "r")

In [23]: archivo_txt.readlines?
Signature: archivo_txt.readlines(hint=-1, /)
Docstring:
Return a list of lines from the stream.

hint can be specified to control the number of lines read: no more
lines will be read if the total size (in bytes/characters) of all
lines so far exceeds hint.
Type:      builtin_function_or_method

In [24]: texto = archivo_txt.readlines()

In [25]: texto
Out[25]: 
['Hola archivos desde Python\n',
 'Hola2 desde Python\n',
 'Hola3 desde Python\n',
 'Hola4 desde Python\n']

In [26]: [linea.replace("\n", "") for linea in texto]
Out[26]: 
['Hola archivos desde Python',
 'Hola2 desde Python',
 'Hola3 desde Python',
 'Hola4 desde Python']

```

### El comando with

A pesar de que podemos utilizar archivos como el ejemplo anterior, se recomienda utilizar el comando *with*, que automaticamente cierra el archivo una vez dejemos de utilizar. Para ellos debemos indentar en un bloque su uso:

`hola_with.py`
```

#La sentencia with coloca la lectura o escritura del archivo en una estructura que lo cierra al terminar
with open("arch2.txt", 'w') as archivo: 
    archivo.write("Primer linea de este archivo\n") 
    archivo.writelines(['Multiples Lineas\n', 'En Lista']) 
                                                                                                                                                 
with open("arch2.txt", 'r') as archivo: 
    print(archivo.readline()) 
    print(archivo.readlines())  
```
