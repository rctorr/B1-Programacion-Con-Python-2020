def imprime_toppings(menu):
    """ Imprime la lista de opciones de toppings """
    print()
    print("-" * 25)
    print(f"{menu[0][0]}. {menu[0][1]}")
    print(f"{menu[1][0]}. {menu[1][1]}")
    print(f"{menu[2][0]}. {menu[2][1]}")
    print(f"{menu[3][0]}. {menu[3][1]}")
    print("-" * 25)

def imprime_precio(opcion):
    """ Imprime el precio del Helado en base al valor de la opcion """
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
