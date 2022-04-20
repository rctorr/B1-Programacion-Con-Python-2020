# 1. Imprimir la lista de opciones en la pantalla
# 2. Leer la opción elegida por el usuario
# 3. En base a la opción del usuario imprimir el valor del helado

print("""
----------------------
1. Helado con oreo
2. Helado con m&m
3. Helado con fresas
4. Helado con brownie
----------------------
""")

opcion_str = input("Elige el topping: ")
opcion = int(opcion_str)

if opcion == 1:
    precio = 19
elif opcion == 2:
    precio = 25
elif opcion == 3:
    precio = 22
elif opcion == 4:
    precio = 28
else:
    precio = 0

if precio == 0:
    print("El Helado elegido no existe!")
else:
    # print("El valor del helado es ${:.2f} M.N.".format(precio))
    print(f"El valor del helado es ${precio:.2f} M.N.")
