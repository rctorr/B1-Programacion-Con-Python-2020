## Importar modulos de la libreris estandar y de librerias externas

### OBJETIVO

- Importar modulos de libreria estandar
- Instalar Pip
- Instalar modulos desde Pip
- Importar modulos externos

#### REQUISITOS

1. Python
2. Pip 
3. Conexión a internet para instalar modulos

#### DESARROLLO

La libreria estandar se incluye preinstalada en python y contiene una serie de modulos para distintos propositos, para utilizarlas usamos la palabra reservada import.

```
# Importar modulos desde la libreria estandar
import os 

# Obteniendo ayuda sobre el modulo, usa  q para salir, jk para moverse arriba / abajo

help(os)

# Usa una función que se encuentra en el modulo, en este caso una lista de directorios
files = os.listdir()
print(files)

# Obteniendo el tamaño de un archivo en kB   

size = os.path.getsize('Readme.md')
print(size)

# Otras maneras de importar modulos
import os.path # Solo algun submodulo, llamando os.path
from os import path # Similar, se llama path directamente
from os import path as pt #importa con alias
```
Adicionalmente, Python poseé una gran cantidad de desarrolladores que han creado distintos modulos. Una forma de acceder a este software es por medio de Pip.

Para instalar Pip ve al siguiente enlace.
https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/
(Sigue las instrucciones de acuerdo a tu SO)

Pip nos permite instalar paquetes desde la terminal, puedes buscar paquetes en: https://pypi.org/

Por ejemplo, para instalar Flask ejecuta en la terminal.
```
$pip install flask
```
Ya instalado lo podemos usar con import 
```
#Despues de instalar flask usando pip, lo podemos importar de forma usual
from flask import Flask
app= Flask(__name__)

#Veremos más sobre Flask en próximas lecciones

```

**Módulos sugeridos para instalar:**

- `ipython`
- `click`

**Haciendo nuestro propio `ls.py`**

Crear el script `ls.py` que imprima la lista de archivos en la salida estándar de la carpeta indicada, si no se indica ninguna carpeta se usará la carpeta actual. Hacer uso del módulo (click)[https://click.palletsprojects.com/en/8.0.x/]. La lista debe incluir el tamaño en bytes, la fecha de modificación y el nombre del archivo

Ejemplo de salida:

```
$ python ls.py 
      4096  09-11-2021 02:40:02   .ipynb_checkpoints
      2256  09-11-2021 02:56:51   Readme.md
      1248  09-11-2021 03:21:45   ls.py

$ python ls.py ../
      4096  02-11-2021 04:58:29   Postwork
      4096  09-11-2021 03:21:45   Ejemplo-02
      4096  02-11-2021 04:59:54   Ejemplo-05
      4096  02-11-2021 02:57:59   .ipynb_checkpoints
      4096  02-11-2021 04:55:02   Reto-04
      4096  02-11-2021 04:50:03   Reto-03
      4096  02-11-2021 04:42:57   Ejemplo-01
       618  02-11-2021 05:01:44   Readme.md
      4096  02-11-2021 04:54:48   Ejemplo-04
      4096  02-11-2021 04:49:53   Ejemplo-03
      4096  02-11-2021 03:04:16   Reto-01
      4096  02-11-2021 04:46:39   Reto-02

$ python ls.py /home/rctorr
      4096  22-05-2020 02:40:55   temp2
      4096  24-04-2021 08:43:46   .synfig
      1821  07-05-2021 18:39:12   .sqlite_history
      4096  06-03-2021 23:05:33   .springlobby
      4254  07-04-2020 17:03:56   .bashrc.bak
...
```
