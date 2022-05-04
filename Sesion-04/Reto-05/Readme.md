 	
## Imprimiendo archivos

### OBJETIVO 

- Crear clases 
- Incluir métodos en las clases
- Incluir constructores
- Utilizar distintos niveles de acceso en la clase

#### REQUISITOS 

1. Python 3
2. Código de reto 3

#### DESARROLLO
Crea un script llamado `tree.py` qie imprima la lista de carpetas y archivos existentes a partir de la carpeta actual del script o de la carpeta proporcionada por el usuario en la línea de comandos.

Sugerencias:
- Usa el módulo click para leer la carpeta inicial proporcionada por el usuario (pregunta como!)
- Crea una clase para archivo
- Crea una clase para carpeta que herede de archivo
- Crea el script para una carpeta que sólo tenga archivos, luego para cuando haya una carpeta y un archivo y luego ya probar con cualquier otra carpeta.

Ejemplo de ejecución:

```
Sesion-04/Reto-05 $ python tree.py
Readme.md

Sesion-04 $ python tree.py
Ejemplo-01/
Ejemplo-02/
Ejemplo-03/
Ejemplo-04/
Postwork/
Reto-01/
Reto-02/
Reto-03/
Reto-04/
Reto-05/
Readme.md
```

