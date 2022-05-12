## Reto 3

### OBJETIVO

- Crear archivos json incluyendo datos de la ejecución del programa

#### REQUISITOS

1. Python 3

#### DESARROLLO

Modifica el script `tree.py` para que incluya la opción `--json` y cree el archivo `salida.json` con la lista de archivos en el directorio indicado en formato JSON siguiente el siguiente formato:

```
$ python tree.py --json carpeta
[
    {
        "tamanio": 741, 
        "nombre": "tree.py", 
        "fecha": "01-012019 10:15:00"
    }, 
    {
        "tamanio": 330, 
        "nombre": "readme.md", 
        "fecha": "10-03-2019 13:17:42"
    },
    ...
]
```
