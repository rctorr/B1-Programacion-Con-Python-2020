
## Postwork 4

### OBJETIVO


- Reforzar los aprendizajes de la sesión 4 y  aplicarlos al proyecto final. Utilizar los conceptos de clase, método y encapsulamiento.

#### REQUISITOS

1. Python 3 

#### DESARROLLO

1. Crea la clase tarjeta de crédito considerando lo siguiente:
   1. Determina los atributos que debería de tener una tarjeta y asignalos con la función constructor (`__init__()`)
   2. Convierte las funciones del módulo tarjeta a métodos
2. Crea la clase usuario y considera lo siguiente:
   1. Los atributos deberán se `nombre` y `tarjetas` donde éste último será una lista de tarjetas para éste usuario.
   2. Crea métodos para `agregar(tarjeta)` y `borrar(nombre de tarjeta)` a la lista
4. Crea constructores, destructores, método __str__ para la clase, que consideres necesarios
5. Haz que los atributos y métodos necesarios sean privados.
6. Crea un script principal para probar el acceso a elementos de la clase

Ejemplo dando de alta tres tarjetas, eliminando la última y luego imprimiendo el reporte de las dos restantes:
```
python pago-tarjeta.py 
Nombre de la tarjeta: Tarjeta1
Tasa de interés anual de la tarjeta (%): 34.5
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar: 255.0
Escribe el monto total de los nuevos cargos: 150.0

Nombre de la tarjeta: Tarjeta2
Tasa de interés anual de la tarjeta (%): 45.0
Escribe el monto de la deuda actual de la tarjeta: 5000.0
Escribe el monto del pago a realizar: 1500.0
Escribe el monto total de los nuevos cargos: 750.0

Nombre de la tarjeta: Tarjeta3
Tasa de interés anual de la tarjeta (%): 41.0
Escribe el monto de la deuda actual de la tarjeta: 3500.0
Escribe el monto del pago a realizar: 1200.0
Escribe el monto total de los nuevos cargos: 300.0

Tarjeta3 dada de baja!


----------------------------------------
---------- Resumen de tarjeta ----------
----------------------------------------
Tarjeta:   Tarjeta1
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
Tarjeta:   Tarjeta2
Tasa de interés anual: 45.00%
----------------------------------------
Deuda actual:             5000.00
Monto del pago:           1500.00
----------------------------------------
Deuda después de pago:    3500.00
Intereses del mes:         131.25
----------------------------------------
Deuda recalculada:        3631.25
Nuevos cargos del mes:     750.00
----------------------------------------
Nueva deuda del mes:      4381.25
```

