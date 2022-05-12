## Archivos .csv

### OBJETIVO

- Crear archivos .csv
- Leer archivos .csv
- Escribir archivos .csv

#### REQUISITOS

1. Python 3

#### PREWORK
Los archivos csv (comma separated values), son un formato de archivos conformados por valores separados por una coma, como si fueran un tabla, son muy usados para almacenar sets de datos.

Existen variantes que usan otro carcter para separar los valores, como lo son los tsv(tab separatted values), que usa tabuladores para separar los valores. Estos últimos suelen utilizarse para almacener corpus de oraciones para análisis de lenguaje natural.

El módulo csv cuenta con clases para facilitar leer y escribir archivos csv.
Funcionan de manera similar a los archivos, con conversión del archivo a listas y viceversa.

La forma de utilizarla, conserva ciertas similitudes con el acceso a otros tipos de archivos

```
In [1]: import csv

In [2]: arch_txt = open("ejemplo.csv")

In [3]: lector_csv = csv.reader(arch_txt)

In [4]: lineas = list( lector_csv )

In [5]: lineas
Out[5]: 
[['Hugo', 'Mc Pato', 'Macho'],
 ['Paco', 'Mc Pato', 'Macho'],
 ['Daisy', 'Mc Pato', 'Hembra']]

In [6]: arch_txt.close()

In [7]: lineas
Out[7]: 
[['Hugo', 'Mc Pato', 'Macho'],
 ['Paco', 'Mc Pato', 'Macho'],
 ['Daisy', 'Mc Pato', 'Hembra']]

In [8]: lineas.append( ["Pluto", "Mc Rey", "Macho"] )

In [9]: lineas
Out[9]: 
[['Hugo', 'Mc Pato', 'Macho'],
 ['Paco', 'Mc Pato', 'Macho'],
 ['Daisy', 'Mc Pato', 'Hembra'],
 ['Pluto', 'Mc Rey', 'Macho']]

In [10]: arch_txt = open("ejemplo.csv", "w")

In [11]: arch_txt.close()

In [12]: with open("ejemplo.csv", "w", newline="") as arch_txt:
    ...:     escritor_csv = csv.writer(arch_txt)
    ...:     escritor_csv.writerows( lineas )
    ...: 

In [13]: with open("ejemplo.csv", "w", newline="") as arch_txt:
    ...:     escritor_csv = csv.writer(arch_txt)
    ...:     escritor_csv.writerow( ["Nombre", "Apellido", "Género"] )
    ...:     escritor_csv.writerows( lineas )
    ...: 

In [14]: 
```

#### DESARROLLO

Ahora modifica el programa `tree.py` de la sesión anterior con los siguiente requerimientos:

1. Agrega la opción `--csv nombre.csv` que permita exportar la información en formato CSV en el archivo `nombre.csv`.
2. Revisa el concepto de segmentar tu programa usando el paradigman de
programación MVC (Nodel View Controler) y crea una función para manejar la
salida en el forma indicado.
3. Comprueba el contenido del archivo CSV abriendolo en el editor de código o en una hoja de cálculo.

Ejemplo de ejecución:

```
Sesion-06/Ejemplo-02 $ python tree.py --csv salida.csv ../
Se ha creado el archivo salida.csv con los resultados.
Sesion-06/Ejemplo-02 $ 
```

