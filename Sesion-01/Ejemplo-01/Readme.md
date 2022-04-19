# Haz tu primera aplicación con python

¡Bienvenido a Python! Python es un lenguaje de programación de alto nivel, fácil de usar, versátil y potente. Es uno de los lenguajes más populares actualmente según el ínidce de TIOBE:


## Objetivo

* Conocer la sintaxis básica de Python, variables y tipos de datos; operadores lógicos y condiciones, así como ciclos de control.

## Usos

Python tiene diversos campos de aplicación, algunas de ellos son:
 - Aplicaciones web (Flask, Django...)
 - Aplicaciones multiplataforma (PyQt, TCL, click..)
 - Aplicaciones móviles (Kivy)
 - Electrónica, IOT (Micropython)
 - Data science (List, NumPy, Pandas, Tensorflow, Scipy...)
 - Robótica (ROS)
 - Vídeojuegos

## Instalación

La instalación dependerá del sistema operativo que tengamos. Para este curso, cualquier versión superior a Python 3.5 es válida para seguirlo, además es importante conocer que la instalación de **Python** se puede realizar de varias formas, sin embargo para éste curso, se instalará la versión conocida como **Python Miniconda**, que inicialmente fué pensado sólo para hacer Ciencia de Datos, pero hoy en día se puede usar para desarrollar cualquier tarea que se necesiten.

El sitio para descargar e instalar es: https://docs.conda.io/en/latest/miniconda.html

En la primer tabla están los links de descarga para cada sistema operativo:

- Para usuarios con MacOSX descargen del link que dice bash al final
- Para usuario con Linux descarguen la que dice sólo Miniconda Linux 64 bit
- Para usuarios con Windows descarguen la que corresponda a su sistema operativo, que hoy en día es casi seguro la que termina en 64-bit.

Ahora para usuarios con Windows se descargará un archivo ejecutable (.exe) que le pueden dar doble click y dar click en siguiente dejado seleccionadas las opciones por omisión hasta que termines el proceso de instalación, para verificar que su instalación ha sido exitosa buscar la aplicación o programa **Anaconda Prompt** y ejecutarlo, esto abrirá una ventana con fondo obscuro conocida como Consola o Terminal donde podremos ejecutar comandos, por ejemplo escribe el siguiente comando y presionar ENTER:

```
C:/users/rctorr> python -V
Python 3.9.5
```
El texto `C:/users/rctorr>` es el prompt o señal del sistema operativo, se imprime en automático y puede cambiar dependiendo de la versión del Window, idioma o configuración.

El texto `python -V` es el comando que deberás de escribir y al terminar presionar la tecla ENTER

El texto `Python 3.9.5` es la respuesta de la ejecución del comando.

También puedes descargar [Ubuntu para Windows 10](https://www.microsoft.com/es-mx/p/ubuntu/9nblggh4msv6), y así tener un sistema Linux en tu equipo accesible desde Windows.

Para usuarios con Linux o MacOSX el procedimiento de instalación no es dando doble click, si no por medio del uso del programa la **Terminal** y la ejecución de algunos comandos como se muestra a continuación, recuerda presionar la tecla ENTER tras escribir cada comando:

1. Abrir la aplicación Terminal
1. Cambiarse a la carpeta de descargas por lo general se puede realizar con el comando: `cd Downloads`
1. Iniciar la instalación con el comando: `bash Miniconda3-latest-MacOSX-x86_64.sh` para usuarios Mac OSX o `bash Miniconda3-latest-Linux-x86_64.sh` para usuarios Linux, esto mostrará la licencia en pantalla que se puede leer presionando la tecla de **Espacio** y luego aceptando los términos.
1. Seguir las indicaciones de la instalación hasta su término usando los valores por defecto cuando se pida escribir algo.
1. Cerrar la ventana de la Terminal y en caso de tener más Terminales abiertas cerrarlas todas, esto con la finalidad de que Miniconda pueda iniciar adecuadamente.
1. Abrir una Terminal nuevamente, entonces al inicio del prompt debe aparecer algo como lo siguiente: `(base) rctorr@gatem:~$`, notar que al inicio dice `(base)` esto es indicativo de que ya está instalado miniconda.
1. También puede verificar la instalación ejecutando el siguiente comando:

```
(base) rctorr@gatem:~$ python -V
Python 3.9.5
```
Donde el texto `rctorr@gatem:~$` es el prompt o señal del sistema operativo, se imprime en automático y puede cambiar dependiendo de la versión del Linux, Mac OS, idioma o configuración.

El texto `python -V` es el comando que deberás de escribir y al terminar presionar la tecla ENTER

El texto `Python 3.9.5` es la respuesta de la ejecución del comando.

---

## Hola mundo

Usualmente, el primer programa que se realiza al aprender un lenguaje es imprimir la frase "Hola Mundo", en Python por ser un lenguaje interpretado es posible ejecutar un programa directamente desde el **Intérprete de Python** usando la Terminal o creando un programa en un archivo con la extensión `.py`.

## Creando un programa y ejecutando desde el Intérprete:

Aunque existe herramientas o IDE's que podrían ejecutar el intérprete dando click en algún menú es bueno conocer como ejecutarlo desde la Terminal o Anaconda Prompt (para usuarios de Windows), así que para iniciar el Intérprete de Python se ejecuta el comando `python`:

```
(base) rctorr@gatem:~$ python
Python 3.9.5 (default, Jun  4 2021, 12:28:51) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
Notar como el prompt cambia de `(base) rctorr@gatem:~$` a `>>>` éste último indica que ya estamos dentro del inerprete de Python y está lista para procesar cualquier instrucción en Python proporcionada, así que vamos a escribir el siguiente código y luego presionamos la tecla **Enter** para ejecutarla, recuerda que aún seguimos en la Terminal.

```
>>> print("Hola mundo de Python")
Hola mundo de Python
>>> 
```

## Creando un programa y ejecutando como archivo

Ahora vamos a crear nuestro primer programa como archivo de Python, para ellos vamos a usar nuestro editor de código (Sublime Texto o cualquier otro), creamos un nuevo archivo, lo guardamos como "hola-mundo.py" en la carpeta `B1-Programacion-Con-Python-2020/Sesion-01/Ejemplo-01` para poder ubicarlo y escribimos el siguiente contenido:

```
print("Hola mundo de Python desde un archivo")
```

Guardamos los cambios y nos pasamos nuevamente a la Terminal, es importante revisar que estamos en la carpeta `B1-Programacion-Con-Python-2020/Sesion-01/Ejemplo-01\`, en caso contrario podemos usar el comando `cd` repetidamente hasta llegar a la carpeta deseada.

Y entonces para ejecutar nuestro programa `hola-mundo.py` usando el comando:

```
(base)[~/Cursos/B1-Programacion-Con-Python-2020/Sesion-01/Ejemplo-01] $ python hola-mundo.py 
Hola mundo de Python desde un archivo
(base)[~/Cursos/B1-Programacion-Con-Python-2020/Sesion-01/Ejemplo-01] $
```

Notar que el comando ejecutado es `python hola-mundo.py` al final de escribirlo presionamos la tecla Enter para ejecutarlo y justo debajo observamos el resultado que no es otra cosa que el mensaje `Hola mundo de Python desde un archivo` que colocamos en la instrucción `print()` de nuestro programa.

Felicidadez, esto seguramente será un pequeño paso para la humanidad pero un gran paso para tí, buen benido al mundo de Python.


