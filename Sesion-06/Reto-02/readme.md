## Reto 2

### OBJETIVO

- Crear archivos csv incluyendo datos de la ejecución del programa

#### REQUISITOS

1. Python 3

#### DESARROLLO

Basándose en el reto anterior, y con el uso de la librería csv, crea un archivo csv, con los siguientes datos:
 *  modelo de auto,
 * color 
 * nivel de equipamiento(bajo, medio,alto)
 * Fecha de captura (no ingresado por el usuario)

 Para obtener la fecha de captura puedes usar datetime.datetime.now() del paquete datetime

```
python autos_csv.py
Inserte nombre del auto: Sentra 
Inserte color: rojo
inserte nivel de equipo:medio
Inserte precio: 190 000 

python autos_csv.py
Inserte nombre del auto: murcielago
Inserte color: negro
inserte nivel de equipo:alto 
Inserte precio: 1200000
```

El archivo `autos.csv` debería contener algo como esto:
```
Sentra,rojo,medio,190 000 ,2020-05-24 21:20:08.790518
murcielago,negro,alto 1200000,1200000,2020-05-24 21:20:36.950413
```
