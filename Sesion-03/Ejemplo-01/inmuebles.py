import csv

def lee_datos(nom_arch):
    """ 
    Lee todos los datos del archivo nom_arch y lo regresa como una lista
    """
    with open(nom_arch) as arch:
        csv_lector = csv.reader(arch)
        lista = list(csv_lector)

    return lista

def imprime_lista(inmuebles):
    """
    Imprime la lista de inmuebles en la salida estándar
    """
    columnas = zip(*inmuebles)
    tamanios = [len(max(col, key=len)) for col in columnas]
    formatos = ["{:"+str(t)+"}" for t in tamanios]
    linea = " ".join(formatos)
    for fila in inmuebles:
        print(linea.format(*fila))
        
def main():
    """ Función principal del script """
    inmuebles: list = lee_datos("inmuebles.csv")

    # Lee lista de palabras, filtra la lista de inmuebles e imprime
    # palabras = lee_palabras()
    # filtrados = filtra_por(inmuebles, palabras[0])

    imprime_lista(inmuebles)

if __name__ == "__main__":
    main()
