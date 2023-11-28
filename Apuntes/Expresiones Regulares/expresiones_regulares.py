import re

texto = """Hola maestro. Esta es la cadena 205 11234 1. cómo estás mi capitán
Esta es la segunda linea de texto.
Esta es la tercera linea de texto.
Y esta es la final definitiva capitán"""
# parámetro flags=re.IGNORECASE para ignorar las mayúsculas.
resultado = re.findall("esta", texto)

# \d -> Busca dígitos númericos del 0 al 9
resultado = re.findall(r"\d", texto)

# \D -> Busca TODO MENOS dígitos númericos del 0 al 9
resultado = re.findall(r"\D", texto)

# \w -> Busca todos los caracteres alfanuméricos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)

# \W -> Busca TODO MENOS los caracteres alfanuméricos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)


# \s -> Busca todos los espacios en blanco (Espacios, tabs, cambios de linea).
resultado = re.findall(r"\s", texto)

# \S -> Busca TODO MENOS los espacios en blanco (Espacios, tabs, cambios de linea).
resultado = re.findall(r"\S", texto)


# \n -> Busca todos los saltos de linea
resultado = re.findall(r"\n", texto)

# . -> Busca TODO MENOS los saltos de linea
resultado = re.findall(r".", texto)

# \ -> Cancela carácteres especiales. Así puedes buscar literalmente algo
resultado = re.findall(r"\.", texto)

# Buscando una cadena que busque un número, seguido de un punto y un espacio.
resultado = re.findall(r"\d\.\s", texto)

# ^ -> Busca el comienzo de una linea
# flags=re.M para multilinea
resultado = re.findall(r"^Esta", texto, flags=re.M)

# $ -> Busca el comienzo de una linea
# flags=re.M para multilinea
resultado = re.findall(r"capitán$", texto, flags=re.M)

# {n} -> Busca n cantidad de veces el valor de la izquierda (En este caso, 3 dígitos juntos)
resultado = re.findall(r"\d{3}", texto)

# {n} -> Busca almenos n y máximo m
resultado = re.findall(r"\d{1,4}", texto)

# | -> -> Busca una cosa o la otra
resultado = re.findall(r"\d{1,4}|Hola", texto)


print(resultado)
