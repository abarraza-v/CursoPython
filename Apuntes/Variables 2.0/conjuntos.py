# Creando un conjunto con set()
conjunto = set(["Dato 1", "Dato 2"])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 3"}

# Teoría de conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {1, 2, 4}

# Verificando si es un subconjunto (Retorna True o False)
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# Verificando si es un superconjunto (Retorna True o False)
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

# Verificar si uno de los elementos coinciden (Retorna True si no hay ninguno que coincida)
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)
