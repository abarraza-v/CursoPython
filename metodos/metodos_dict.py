diccionario = {"nombre": "Alejandro", "apellido": "Barraza", "año": 2005}

# Devuelve un objeto dict_item
claves = diccionario.keys()

# Devuelve un objeto dict_item iterable por un bucle
diccionario_iterable = diccionario.items()

# Obteniendo un elemento con get()
# Si este método no encuentra nada, devuelve "None" en vez de parar el código con un error.
valor_de_aaa = diccionario.get("aaa")

# Eliminar un elemento del diccionario
diccionario.pop("apellido")


print(diccionario_iterable)

# Eliminar todo el diccionario
diccionario.clear()
