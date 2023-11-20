# Crear función que nos devuelva los números primos entre 0 y el argumento que pasamos.
import math


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


def primos_hasta(num):
    primos = list()
    for i in range(num + 1):
        resultado = es_primo(i)
        if resultado:
            primos.append(i)
    return primos


num = int(input("Ingresa un número y te diré si es primo.  "))

if es_primo(num):
    print("tu número es primo")
else:
    print("tu número no es primo")

print(primos_hasta(11))
