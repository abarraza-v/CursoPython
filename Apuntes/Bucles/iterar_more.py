frutas = ["pera", "manzana", "naranja", "palta", "durazno", "granada"]
cadena = "Alejandro"
numeros = [10, 24, 12, 30]

# Evitar uno de los ciclos
for fruta in frutas:
    if fruta == "durazno":
        continue
    print(f"Me comí una {fruta}")
else:
    print("El bucle acabó")
print("-----------------------------")

# Parar el ciclo
for fruta in frutas:
    print(f"Me comí una {fruta}")
    if fruta == "palta":
        print(f"La última fruta que me comí me hizo mal, ya no puedo comer más.")
        break
else:  # Break ignora incluso el else.
    print("El bucle acabó")

# Recorrer una cadena de texto
for letra in cadena:
    print(letra)

# For en una sola linea de código
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
