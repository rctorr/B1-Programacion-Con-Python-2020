
## Operadores aritmeticos y lógicos

### OBJETIVO

- Utilizar operadores lógicos.
- Utilizar operadores aritmeticos.

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los operadores aritmeticos permiten realizar operaciones aritmeticas con datos enteros o flotantes.

![imagen](https://static.platzi.com/media/user_upload/1-a5257be9-296d-40be-b7bf-3885edead804.jpg)

Los operadores lógicos trabajn con valores de verdad (True y False), y son equivalentes a las compuertas lógicas AND, OR y NOT.

Antes de pasar a escribir nuestro programa, vamos a experimentar unos momentos usando el Intérprete de Python que a estas altura ya lo deberías de tener abierto como una ventana adicional, recuerda que para desarrollar en Python se estila tener 2 ventana de tipo Terminal, una con el Intérprete de Python ejecutando, otra para ejecutar nuestros programas y la tercera es la ventana de nuestro editor de código.

Ahora si pasamos a crear el archivo `operadores.py` con el siguiénte código para comprobar el funcionamiento de ciertos operadores.

```
operando1 = 6
operando2  = 10
incremento = 0

# Operadores aritmeticos
suma = operando1 + operando2
print("La suma de los valores es:")
print(suma)

producto = operando1 * operando2
print("El resultado de la multiplicacion es")
print(producto)

producto = operando1 / operando2
print("El división de la multiplicacion es")
print(producto)

incremento += 1
print("El resultado es")
print(incremento)

#Operadores lógicos
operando3 = True
operando4 = False

compuerta_and = operando3 and operando4
print("El resultado de la AND es")
print(compuerta_and)

negando = not operando3
print("Esto es una negación")
print(negando)
```







