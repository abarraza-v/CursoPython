cadena1 = "Hola soy Alejandrino"
cadena2 = "Bienvenido Robertonto eres muy tonto"

# Función dir devuelve la lista de atributos válidos del objeto.
dir = dir(cadena1)

# Para convertir a mayúscula
mayuscula = cadena1.upper()

# Para convertir a minúscula
minuscula = cadena1.lower()

# Primera letra en mayúscula
primer_letra_mayuscula = cadena1.capitalize()

# Buscar una cadena en otra cadena (Si no hay coincidencias devuelve -1)
busqueda_find = cadena1.find("a")

# Buscar una cadena en otra cadena (Si no hay coincidencias lanza una excepción)
busqueda_index = cadena1.index("d")

# Verifica si el dato es númerico (independiente de si es string o int) devuelve True o False.
es_numerico = "1".isnumeric()

# Verifica si el datos es alfanumérico (solo carácteres de la a hacia la z) devuelve True o False.
es_alfanumerico = "alejandrino 5".isalpha()

# Buscar una cadena en otra cadena. Devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

# Función que cuenta la cantidad de caracteres de una cadena.
contar_caracteres = len(cadena1)

# Verificar que empieza con x cadena de carácteres. Devuelve True o False
empieza_con = cadena1.startswith("Hola")

# Verificar que termina con x cadena de carácteres. Devuelve True o False
termina_con = cadena1.endswith("o")

# Reemplazar un pedazo de la cadena enviada (El parámetro 1 es el pedazo que queremos reemplazar, y el parámetro 2 es el que lo reemplazará)
cadena_nueva = cadena1.replace("la", "lu")

# Separar cadenas por cadena clave. Devuelve una lista con los valores.
cadena_separada = cadena2.split(" ")

print(cadena_separada[0])
