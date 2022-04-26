## Postwork 3

### OBJETIVO

- Reforzar los aprendizajes de la sesión 3 y  aplicarlos al proyecto final. Utilizar los conceptos de args, modulos, paquetes y docstrings.

#### REQUISITOS

1. Python 3

#### DESARROLLO

1. Crea un paquete, dentro del cual tendras 2 modulos:
        - Usuario: contiene la función multiples_reportes
        - tarjeta: Incluye el resto de funciones
2. Agrega una función que pueda proyectar multiples pagos distintos sobre una tarjeta a traves de los meses, colocala en el modulo tarjeta
3. Agrega docstrings para todas las funciones
4. Crea un archivo externo desde el cual puedas probar el acceso a las funciones que estan dentro del paquete

Ejemplo de lista de archivos esperados:

```
├── pago-tarjeta.py
└── tarjeta
    ├── __init__.py
    ├── tarjeta.py
    └── usuario.py
```

Ejemplo de ejecución capturando tres tarjetas e imprimiendo su resumen:

```
python pago-tarjeta.py 
Nombre de la tarjeta: Visa
Tasa de interés anual de la tarjeta (%): 34.5
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar: 255.0
Escribe el monto total de los nuevos cargos: 150.0

Nombre de la tarjeta: American
Tasa de interés anual de la tarjeta (%): 45.0  
Escribe el monto de la deuda actual de la tarjeta: 5000.0
Escribe el monto del pago a realizar: 3500.0
Escribe el monto total de los nuevos cargos: 1500.0

Nombre de la tarjeta: Master
Tasa de interés anual de la tarjeta (%): 41.0  
Escribe el monto de la deuda actual de la tarjeta: 3400
Escribe el monto del pago a realizar: 1200
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
Deuda actual:             5000.00
Monto del pago:           3500.00
----------------------------------------
Deuda después de pago:    1500.00
Intereses del mes:          56.25
----------------------------------------
Deuda recalculada:        1556.25
Nuevos cargos del mes:    1500.00
----------------------------------------
Nueva deuda del mes:      3056.25



----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Master
Tasa de interés anual: 41.00%
----------------------------------------
Deuda actual:             3400.00
Monto del pago:           1200.00
----------------------------------------
Deuda después de pago:    2200.00
Intereses del mes:          75.17
----------------------------------------
Deuda recalculada:        2275.17
Nuevos cargos del mes:     500.00
----------------------------------------
Nueva deuda del mes:      2775.17
```

Ejemplo obteniendo el pago recurrente para la primer tarjeta del ejemplo anterior:
```
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

Ejemplo de proyectar varios pagos distintos a un tarjeta:
```
python pago-tarjeta.py 
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

Escribe la cantidad del siguiente pago (escribe 0 para terminar): 300.0

Escribe la cantidad del siguiente pago (escribe 0 para terminar): 200.0

Escribe la cantidad del siguiente pago (escribe 0 para terminar): 350.0

Escribe la cantidad del siguiente pago (escribe 0 para terminar): 0


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
Monto del pago:            300.00
----------------------------------------
Deuda después de pago:     616.42
Intereses del mes:          17.72
----------------------------------------
Deuda recalculada:         634.14
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:       634.14


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:              634.14
Monto del pago:            200.00
----------------------------------------
Deuda después de pago:     434.14
Intereses del mes:          12.48
----------------------------------------
Deuda recalculada:         446.62
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:       446.62


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta a nombre de:   Visa
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:              446.62
Monto del pago:            350.00
----------------------------------------
Deuda después de pago:      96.62
Intereses del mes:           2.78
----------------------------------------
Deuda recalculada:          99.40
Nuevos cargos del mes:       0.00
----------------------------------------
Nueva deuda del mes:        99.40
```