## Postwork 2

### OBJETIVO

- Reforzar los aprendizajes de la sesión 2 y  aplicarlos al proyecto final. Utilizar los conceptos de función, ciclos y estructuras de datos.

#### REQUISITOS

1. Python 3

#### DESARROLLO

Apoyate en el desarrollo de el postwork pasado para crear las siguientes funciones:
1. Crea la función `crea_tarjeta()`, esta debe realizar lo siguiente:
   1. Contener la captura de datos de una tarjeta
   2. Devolver un diccionario con la información.
   3. En caso de que se indique un monto mayor de pago del posible, debe indicar el error con un mensaje y solicitar la informacion nuevamente.
2. Crea la funcion `captura_nueva_deuda(tarjeta_dict)` y debe realizar:
   1. Recibir un diccionario con los datos de una tarjeta
   2. Hacer los calculos vistos en el postwork1
   3. Agregar la nueva deuda como un dato adicional del diccionario.
3. Crea la función `generar_reporte(tarjeta_dict)`, este debe realizar:
   1. Recibir un diccionario con los datos de una tarjeta
   2. Imprimir el reporte como en el postwork1
4. Crea una función que:
   1. Reciba una lista de tarjetas
   2. Itere sobre la lista e imprima los reportes de cada una
5. Crea la función `pago_recurrente(tarjeta_dict)`, la cual hara:
   1. Recibir un diccionario con los datos de una tarjeta
   1. Proyectara una serie de pagos del mismo monto en una tarjeta hasta convertir el valor de la deuda en 0
   1. Considerar que no habrá nuevos cargos
   1. Para cada mes proyectado se debe imprimir el reporte correspondiente.
6. Haz llamadas y prueba las funciones que has creado

Caso de ejemplo para una lista de tarjetas:
```
python tarjeta.py 
Nombre de la tarjeta: Visa
Tasa de interés anual de la tarjeta (%): 34.5
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar: 255.0
Escribe el monto total de los nuevos cargos: 150.0

Nombre de la tarjeta: American
Tasa de interés anual de la tarjeta (%): 45.0
Escribe el monto de la deuda actual de la tarjeta: 15000.0
Escribe el monto del pago a realizar: 3500.0
Escribe el monto total de los nuevos cargos: 2750.0

Nombre de la tarjeta: Master
Tasa de interés anual de la tarjeta (%): 40.0
Escribe el monto de la deuda actual de la tarjeta: 5000.0
Escribe el monto del pago a realizar: 2500.0
Escribe el monto total de los nuevos cargos: 500.0


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:             1000.00
Monto del pago:            255.00
----------------------------------------
Deuda después de pago:     745.00
Intereses del mes:          21.42
----------------------------------------
Deuda recalculada:         766.42
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:       916.42



----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   American
Tasa de interés anual: 45.00%
----------------------------------------
Deuda actual:            15000.00
Monto del pago:           3500.00
----------------------------------------
Deuda después de pago:   11500.00
Intereses del mes:         431.25
----------------------------------------
Deuda recalculada:       11931.25
Nuevos cargos del mes:    2750.00
----------------------------------------
Nueva deuda del mes:     14681.25



----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Master
Tasa de interés anual: 40.00%
----------------------------------------
Deuda actual:             5000.00
Monto del pago:           2500.00
----------------------------------------
Deuda después de pago:    2500.00
Intereses del mes:          83.33
----------------------------------------
Deuda recalculada:        2583.33
Nuevos cargos del mes:     500.00
----------------------------------------
Nueva deuda del mes:      3083.33
```

Caso de ejemplo para la función `pago_recurrente()`:
```
python tarjeta.py 
Nombre de la tarjeta: Visa
Tasa de interés anual de la tarjeta (%): 34.5
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar: 255.0
Escribe el monto total de los nuevos cargos: 150.0

----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:             1000.00
Monto del pago:            255.00
----------------------------------------
Deuda después de pago:     745.00
Intereses del mes:          21.42
----------------------------------------
Deuda recalculada:         766.42
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:       916.42


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:              916.42
Monto del pago:            255.00
----------------------------------------
Deuda después de pago:     661.42
Intereses del mes:          19.02
----------------------------------------
Deuda recalculada:         680.43
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:       680.43


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:              680.43
Monto del pago:            255.00
----------------------------------------
Deuda después de pago:     425.43
Intereses del mes:          12.23
----------------------------------------
Deuda recalculada:         437.67
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:       437.67


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:              437.67
Monto del pago:            255.00
----------------------------------------
Deuda después de pago:     182.67
Intereses del mes:           5.25
----------------------------------------
Deuda recalculada:         187.92
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:       187.92


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:              187.92
Monto del pago:            187.92
----------------------------------------
Deuda después de pago:       0.00
Intereses del mes:           0.00
----------------------------------------
Deuda recalculada:           0.00
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:         0.00
```


