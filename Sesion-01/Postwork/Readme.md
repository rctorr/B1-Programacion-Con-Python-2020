
## Postwork 1

### OBJETIVO

-Reforzar los aprendizajes de la sesión 1 y  aplicarlos al proyecto final. Trazar requerimientos, así como utilizar los conceptos de variables, condicionales, cadenas de texto y formatos en su proyecto personal.
#### REQUISITOS

1. Python 3

#### DESARROLLO

- Haz un programa que solicite al usuario los siguientes datos
        - Nombre de la tarjeta

        - Tasa de interés

        - Deuda

        - Pago a realizar

        - Nuevos cargos
        
- El programa deberá devolver un resumen de la información y calcular el monto del próximo pago mensual.
- El programa deberá considerar que no es posible realizar un pago superior al total de la deuda del mes pasado.
- Para los fines de este trabajo, considera las siguientes fórmulas.
        interes_mensual = tasa_interes/12
        deuda_recalculada = (deuda - pago)*(1+interes_mensual)
        nueva_deuda = deuda_recalculada + cargos

Define cómo resolverías el problema con los conceptos vistos en clase.
Utiliza variables, y define sus nombres. Usa condicionales e input de ser necesario.
Agrega formato a la información a mostrar, utilizando todas las bondades de format(). 
Revisa https://pyformat.info para conocer todos sus usos.
Empuja a Github los cambios para revisarlos la próxima clase.

Ejemplos de ejecución:

```
python tarjeta.py 
Nombre del dueño de la tarjeta: Hugo
Tasa de interés anual de la tarjeta (%): 35.0
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar: 1200.0

No es posible realizar un pago mayor a la deuda!


python tarjeta.py 
Nombre del dueño de la tarjeta: hugo
Tasa de interés anual de la tarjeta (%): 34.5
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar: 250.0
Escribe el monto total de los nuevos cargos: 150.0

Resumen de tarjeta:
----------------------------------------
Tarjeta a nombre de:   hugo
Tasa de interés anual: 34.50%
----------------------------------------
Deuda actual:             1000.00
Monto del pago:            250.00
----------------------------------------
Deuda después de pago:     750.00
Intereses del mes:          21.56
----------------------------------------
Deuda recalculada:         771.56
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:       921.56
```
