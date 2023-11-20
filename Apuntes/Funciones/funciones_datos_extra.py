def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"


# utilizando keywords arguments
frase_resultante = frase(adjetivo="alto", nombre="Alejandrino", apellido="Barraziña")
print(frase_resultante)


# Creando misma función con un parámetro opcional que ya tiene valor por defecto.
def frase_alternativa(nombre, apellido, adjetivo="tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"


frase2_resultante = frase_alternativa(
    "Alejandrino", "B", "inteligente"
)  # El tercer parámetro es opcional.
print(frase2_resultante)
