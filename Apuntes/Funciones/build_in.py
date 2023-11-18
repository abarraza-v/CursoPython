numeros = [4, 7, 1, 42, 15]

# Encontrar el número mayor de una lista (Tira error si no le envían números)
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrar el número mayor de una lista (Tira error si no le envían números)
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondear decimales
numero = round(12.3454678, 2)

# Retorna False -> 0, vacío, False, None / Retorna True -> distinto a 0, True, cadena, datos no vacíos
resultado_bool = bool("asdasd")

print(resultado_bool)

# Retorna True si todos los valores de un iterable son verdaderos
resultado_all = all([1, True, "asdas", [123123, 3123]])
print(resultado_all)

# Sumar todos los valores de un iterable (Tira error si no le envían números)
resultado_sum = sum(numeros)
print(resultado_sum)
