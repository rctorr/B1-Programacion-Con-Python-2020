## Tuplas

### OBJETIVO

- Declarar tuplas
- Acceder a datos mediante indices
- Identificar la inmutabilidad de las tuplas y sus implicaciones

#### REQUISITOS

1. Python 3

#### DESARROLLO

Las tuplas son estructuras de datos  similares a las listas, pero que se caracterizan por ser inmutables.

Formas de declarar una tupla

```
# Creando una tupla vacia
t1 = ()
t2 = tuple()


# Tupla de un elemento

t3 = (1, )  # Sin la coma no se detecta como tupla

```

Se pueden asignar de forma simultanea los valores de una tupla a variables.
```
# Asignacion multiple con tupla

a, b = (10, 20)

```

Las tuplas son inmutables, por lo que el intentar modificarlas es causa de error.
```
#No se puede modificar una tupla, quitar comentarios para comprobar

t1.insert(0, 1)
t1.append(10)
```
Pero si podemos acceder a los valores almacenados
```
a = t3[0]
```
O convertir a listas, las cuales si se pueden modificar
```
l1 = list(t3)
```

Modifica el script (programa) `helado.py` de la Sesion-01 para que ahora el menú de toppings sea creado con una tupla de tuplas, el resultado será el mismo pero la forma de obtenerlo será diferente, a este proceso se le conoce como **Refactorización**.

Ejemplo de ejecución:

```
python helado.py 

----------------------
1. Helado con oreo
2. Helado con m&m
3. Helado con fresas
4. Helado con brownie
----------------------
Elige el topping: 4
El valor del helado es $28.00 M.N.
```
