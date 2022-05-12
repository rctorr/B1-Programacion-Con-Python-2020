import producto

# Variables generales

# Variables glbales
MENU = (
    (1, "Adicionar un producto"),
    (2, "Eliminar un producto"),
    (3, "Modificar un producto"),
    (4, "Importar una lista de productos desde una BD SQLite3"),
    (5, "Exportar la lista de productos a una BD SQLite3"),
    (6, "Importar una lista de productos desde un archivo CSV"),
    (7, "Exportar la lista de productos a un archivo CSV"),
    (8, "Importar una lista de productos desde un archivo JSON"),
    (9, "Exportar la lista de productos a un archivo JSON"),
    (0, "Salir"),
)

def imprimir_menu():
    """ Imprime el menú de la aplicación y lee la respuesta del
    usuario.
    """
    print()
    print("-" * 60)
    for i, texto in MENU:  # opcion = (0, "Salir")
        print(f"{i}. {texto}")
    print("-" * 60)
    respuesta_str = input("Elige una opción: ")
    try:
        respuesta = int(respuesta_str)
    except ValueError:
        respuesta = -1

    return respuesta


def main():
    """ función principal del programa """
    productos = []  # Lista de productos de tipo Producto
    continuar = True
    while continuar:
        producto.imprimir_productos(productos)
        opcion = imprimir_menu()
        if opcion == 1:  # Adicionar un producto
            producto.agrega_producto(productos)
        elif opcion == 2:  # Eliminar un producto
            producto.elimina_producto(productos)
        elif opcion == 8:  # Importar de JSON
            productos = producto.importar_de_json()
        elif opcion == 9:  # Exportar a JSON
            producto.exportar_a_json(productos)
        elif opcion == 0:  # Salir de programa
            continuar = False
            print("El programa ha terminado!")
        else:  # opcion = -1, osea inválida!
            print("La opción elegida no es válida!")

if __name__ == '__main__':
    main()