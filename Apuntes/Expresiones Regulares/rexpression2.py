import re

text = """Este es un ejemplo para sacar una página web de esta cadena de carácteres
http://example.com"""

# para que la URL sea válida, tiene que empezar con http o https. (la S es opcional)
# luego tiene que tener :// y carácteres de la a-z en minúsculas o mayúsculas,
# dígitos del 0 al 9, puntos y guiones medios almenos UNA VEZ.
# Tiene que seguir con un punto y con almenos 1 carácter de la a-z minúscula o mayúscula.
pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)
