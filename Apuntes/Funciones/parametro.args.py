# Utilizando el operador * como argumento (* = args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus números es {sum(numeros)}"


resultado = suma("Ale", 1, 2, 3, 1, 5, 7, 10)
print(resultado)
