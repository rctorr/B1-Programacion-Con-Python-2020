import click
# import ...

class Carpeta():
    pass

def imprime_elementos(lista):
    pass

@click.command()
@click.argument("carpeta", default=".")
def main(carpeta):
    """
    Imprime la lista de archivos y carpetas de la carpeta actual o de la
    CARPETA proporcionada por el usuario.
    """
    print("Valor de la variable carpeta =", carpeta)

    obj_carpeta = Carpeta(carpeta)
    lista_elementos = obj_carpeta.obtener_lista_elementos()
    imprime_elementos(lista_elementos)


if __name__ == '__main__':
    main()
