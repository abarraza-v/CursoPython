frutas = ["pera", "manzana", "naranja", "palta", "durazno", "granada"]

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
