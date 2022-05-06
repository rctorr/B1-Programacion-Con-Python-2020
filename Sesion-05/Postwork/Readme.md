
## Postwork 5

### OBJETIVO

- Reforzar los aprendizajes de la sesión 5 y  aplicarlos al proyecto final. Herencia, polimorfismo, decoradores y control de excepciones.
#### REQUISITOS

1. Python 3

#### DESARROLLO

1. Crea la clase `Tarjeta_de_servicios` en un nuevo módulo con lo siguiente:
   1. Heredará desde `Tarjeta`: Una tarjeta de servicios es un tipo especial de tarjeta
   2. Solamente permite realizar pagos totales de la deuda
   3. No aplica una tasa de interes sobre saldos remanentes ya que son cero
   4. Sobrecarga los métodos necesarios para solo permitir pagos totales
   5. Usa try y except para evitar que un usuario introduzca argumentos no validos en el método crea_tarjeta

2. Crea la clase `TarjetaDB` que permita:
   1. Inicializar la conexión a una base de datos SQLite3
   2. Crear la tabla `Tarjeta` si no existiese en la base de datos
   3. Insertar una tarjeta a la base de datos
   4. Obtener la lista de las tarjetas en la base de datos
   5. Crear un script que permita agregarlos datos de 3 tarjetas a la base de datos y luego imprimir los datos de las 3 tarjetas de forma tabular haciendo uso de la clase `Tarjeta`.


Ejemplo de operaciones realizadas con una Tarjeta de servicios:
```
python pago-tarjeta.py 
Nombre de la tarjeta: Comer
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar (sólo se hacepta un pago igual a la deuda): 0
Escribe el monto total de los nuevos cargos: 150.0


----------------------------------------
--------- Tarjeta de servicios ---------
----------------------------------------
Tarjeta:   Comer
----------------------------------------
Deuda actual:             1000.00
Monto del pago:              0.00
----------------------------------------
Deuda recalculada:        1000.00
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:      1150.00

Escribe la cantidad del pago: 0
Sólo es posible realizar un pago igual a la deuda actual!

Escribe la cantidad del pago: 1000.0


----------------------------------------
--------- Tarjeta de servicios ---------
----------------------------------------
Tarjeta:   Comer
----------------------------------------
Deuda actual:             1000.00
Monto del pago:           1000.00
----------------------------------------
Deuda recalculada:           0.00
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:       150.00

```

Ejemplo de operaciones realizadas con `TarjetaDB`:

```
python tarjetadb.py 
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

Lista de tarjetas en la base de datos:
----------------------------------------------------
Nombre   Tasa (%) Deduda    Pago      Nuevos cargos
----------------------------------------------------
Tarjeta1     34.5   1000.00    250.00        150.00
Tarjeta2     45.0   5000.00   1500.00        750.00
Tarjeta3     41.0   3500.00   1200.00        300.00
----------------------------------------------------
