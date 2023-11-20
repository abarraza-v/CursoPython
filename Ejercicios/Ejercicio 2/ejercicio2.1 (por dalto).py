def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero:  ")
        edad = int(input("ingrese la edad del compañero:  "))
        compañero = nombre, edad
        compañeros.append(compañero)
    # El método sort, en una lista de tuplas, ordena según el primer elemento de las tuplas.
    # En este caso, se modifica ese comportamiento por defecto mediante una función lambda
    # y el parámetro key=.
    # El método sort envía los elementos de compañeros a la función lambda, la cuál retorna
    # el valor [1] de cada tupla.
    # Entonces, el método sort ordenará según el segundo elemento de las tuplas. (la Edad).
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    # Al utilizar -1, es como decir "el último elemento de la lista"
    profesor = compañeros[-1][0]
    return asistente, profesor


asistente, profesor = obtener_compañeros(2)

print(f"El profesor es: {profesor} y su asistente es {asistente}")
