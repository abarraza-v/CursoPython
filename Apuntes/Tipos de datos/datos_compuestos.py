# Creando una lista (Es modificable)
lista = ["Roberto", "Zuñiga", True, 1.60]

# Creando una tupla (No es modificable el orden ni los elementos)
tupla = ("Roberto", "Zuñiga", True, 1.60)

# Creando un conjunto (No es modificable los elementos y no se puede acceder por índice)
# En un conjunto no pueden haber datos duplicados
conjunto = {"Roberto", "Zuñiga", True, 1.60}

# Creando un diccionario (dict)
# El primer dato es la "key" y el segundo es el "value"
# No se puede acceder por index
diccionario = {
    "nombre": "Alejandrino",
    "apellido": "Barraza",
    "es_feliz": True,
    "altura": 1.75,
}

print(diccionario["nombre"])
