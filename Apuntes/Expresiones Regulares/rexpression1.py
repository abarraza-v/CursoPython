import re

email = "asad123@gmail.com"


# Correo sin espacios, solo alfanuméricos, guiones, porcentajes, puntos y símbolo más.
# un arroba, seguido de caracteres alfanuméricos, puntos y guión medio.
# Luego un punto seguido de caracteres de la a-z mayúscula o minúscula de almenos 2 de largo.
pattern = r"[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print("Dirección de correo válida")
else:
    print("Dirreción de correo inválida")
