numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 20]


# Las funciones lambda retornan valores automáticamente.
# Muy útiles para hacer cosas sencillas y rápidas.
# Para trabajos más complejos es mejor utilizar una función normal.

# Creando una función lambda para multiplicar por dos
multiplicar_por_dos = lambda x: x * 2


# Creando función común que diga si un número es par o no.
def es_par(num):
    if num % 2 == 1:
        return False
    return True


# Usando filter con una función común
numeros_pares = filter(es_par, numeros)

# Haciendo lo anterior con lambda
lambda_pares = filter(lambda numero: numero % 2 == 0, numeros)

print(list(lambda_pares))
