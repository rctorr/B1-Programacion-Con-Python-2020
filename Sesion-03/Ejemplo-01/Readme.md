## Args y kwargs
### OBJETIVO 

- Obtener un numero de argumentos no determinado usando args
- Obtener argumentos con nombre usando kwargs

#### REQUISITOS 

1. Python 3 

#### DESARROLLO

Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente. 

Para obtener un número indeterminado de argumentos usamos *args, los argumentos en *args se consideran una tupla y se puede iterar sobre ellos.
```
def imprime(*a2gs):  
    for arg in a2gs:  
        print (arg) 
    
imprime('Hola', 'A', 'Todos', '!')
```
Se pueden mezclar argumentos comunes con args
```
def imprime_varias_veces(veces, *argv): 
    for i in range(veces):
        for arg in argv:
            print(arg)

  
imprime_varias_veces(3, 'Bienvenidos ', 'a', 'Bedu') 
```
**kwargs nos permite pasar argumentos nombrados (también un número indeterminado)
```
def saludo(**kwargs):
    print('Hola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))

saludo(empresa='Bedu',nombre='Luis')
saludo(nombre='Luis',empresa='Bedu')
```
Los valores se tratan como un diccionario y se pueden utilizar sus llaves y valores
```
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
myFun(nombre ='Fernando', empresa ='Bedu', ciudad='CDMX') 
```

**Ejemplo:** Modifica el script `inmuebles.py` para que solicite el **Tipo** de inmueble al usuario desde la entrada estándar, ejecutar el script para ver tipos de inmuebles disponibles. El usuario deberá poder indicar uno, dos o más tipos de inmuebles, entonces se deberá imprimir la lista de inmuebles cuyo tipo coincida con los indicados por el usuario.

Resultado de ejemplo:

```
python inmuebles.py 
Escribe los tipos de inmuebles separados por un espacio: Industrial Oficina Parking
Referencia Fecha Alta Tipo       Operación Provincia Superficie Precio Venta Fecha Venta Vendedor
1          01/01/04   Parking    Alquiler  Lleida    291        2133903      19/06/04    Carmen  
3          01/01/04   Oficina    Alquiler  Girona    82         712416       08/11/04    Joaquín 
4          02/01/04   Parking    Alquiler  Girona    285        1815450      27/04/04    Jesús   
6          03/01/04   Industrial Alquiler  Girona    131        953156       05/09/04    Pedro   
7          03/01/04   Parking    Alquiler  Tarragona 69         406686       07/06/04    Pedro   
...
```
