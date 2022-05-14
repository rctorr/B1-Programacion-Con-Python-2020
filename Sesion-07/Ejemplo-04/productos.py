"""
Módulo productos.py

Contiene funciones para manipular una lista de productos como un archivo JSON.
"""

import json

NOMBRE_JSON = "productos.json"

def lista_productos():
    """ Regresa la lista de productos en el archivo json """
    try:
        with open(NOMBRE_JSON) as arch_txt:
            productos = json.load(arch_txt)
    except FileNotFoundError:
        productos = []
        
    return productos

def alta(nombre, precio, descripcion):
    """ Da de alta el producto en el archivo json """
    try:
        with open(NOMBRE_JSON) as arch_txt:
            productos = json.load(arch_txt)
    except FileNotFoundError:
        productos = []
    id_ = len(productos)
    productos.append(
        {
            "id": id_,
            "nombre": nombre,
            "precio": precio,
            "descripcion": descripcion
        }
    )
    with open(NOMBRE_JSON, "w") as arch_txt:
        json.dump(productos, arch_txt, indent=4)
    
def modificar(id_, nombre, precio, descripcion):
    """ Modifica un producto en el archivo json """
    with open(NOMBRE_JSON) as arch_txt:
        productos = json.load(arch_txt)
    for producto in productos:
        if producto["id"] == id_:
            producto["nombre"] = nombre
            producto["precio"] = precio
            producto["descripcion"] = descripcion
            break
    with open(NOMBRE_JSON, "w") as arch_txt:
        json.dump(productos, arch_txt, indent=4)
    
