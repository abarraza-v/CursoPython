animales = ["gato", "perro", "loro", "cocodrilo", "caballo"]
numeros = [100, 42, 60, 23, 20, 10, 40]

# Recorriendo listas
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

for numero in numeros:
    resultado = numero * 10
    print(resultado)

# Recorrer dos listas a la vez del mismo tamaño
for animal, numero in zip(animales, numeros):
    print(f"Recorriendo lista animales: {animal}")
    print(f"Recorriendo lista números {numero}")

for num in range(10, 20):
    print(num)

# Forma no óptima de recorrer una lista con su índice
for num in range(len(numeros)):
    print(numeros[num])

# Forma correcta de recorrer una lista con su índice
# Los conjuntos no tienen índice.
for i, num in enumerate(numeros):
    print(i, num)

# Usando else
for numero in numeros:
    print(numero)
else:
    print("el bucle terminó")

# Sirve exactamente igual en listas tuplas y conjuntos.
