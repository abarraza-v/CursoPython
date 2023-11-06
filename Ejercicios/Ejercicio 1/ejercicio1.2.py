frase = input("Dime cualquier frase real y calcularé en cuanto tiempo la dirías  ")

palabras = frase.split(" ")
cantidad_de_palabras = len(palabras)
secs_necesarios_para_frase = cantidad_de_palabras * 10 // 2 / 10
secs_dalto_diría = cantidad_de_palabras * 10 // 2.6 / 10


print(f"Tu frase tiene {cantidad_de_palabras} palabras.")
if secs_necesarios_para_frase > 60:
    print("Amigo, tampoco te pedí un testamento")

print(
    f"Aproximadamente tardarás {secs_necesarios_para_frase} segundos en decir tu frase."
)
print(
    f"Ya que dalto habla un 30% más rápido, aproximadamente él necesitaría {secs_dalto_diría} segundos para decir tu frase"
)
