# Creando diccionario con dict()
diccionario = dict(nombre="Alejandro", apellido="B")

# Las listas no pueden ser claves, sin embargo las tuplas y conjuntos frozen sí.
diccionario = {("alejandro", "b"): "nada"}

# creando diccionarios con fromkeys() valor por defecto: none
# Primer parámetro tiene que ser iterable. con el segundo podemos cambiar el valor por defecto.
diccionario = dict.fromkeys(["nombre", "apellido"])

# Creando diccionario con valor por defecto: A
diccionario = dict.fromkeys(["nombre", "apellido"], "A")

print(diccionario)
