diccionario = {"nombre": "Alejandro", "apellido": "Barraza", "año": 2005}

# Devuelve un objeto dict_item
claves = diccionario.keys()

# Devuelve un objeto dict_item iterable por un bucle
diccionario_iterable = diccionario.items()

# Obteniendo un elemento con get() (recibe como parámetro la key)
# Si este método no encuentra nada, devuelve "None" en vez de parar el código con un error.
valor_de_aaa = diccionario.get("nombre")

# Eliminar un elemento del diccionario
diccionario.pop("apellido")


print(valor_de_aaa)

# Eliminar todo el diccionario
diccionario.clear()
