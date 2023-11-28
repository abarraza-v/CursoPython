import re

# Detectar un número chileno y ocultarlo.

texto = "Hola Roberto, mi numero es +56951544551"

patron = r"\+56.?9.?\d{1,8}"

numerodetectado = re.findall(patron, texto)

textoconnumerooculto = re.sub(patron, "(número oculto)", texto)

print(textoconnumerooculto)
