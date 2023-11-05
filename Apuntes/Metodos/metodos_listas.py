# Crear una lista (Es una buena práctica crear listas vacías con esta función)
lista = list()

lista = [200, 120]

# Función len (length) Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# Agregar un elemento al final de la lista
lista.append(100)

# Agregar un elemento a la lista en un index específico
lista.insert(1, "Ola")

# Agregar varios elementos al final de la lista
lista.extend([1000, 500])

# Eliminar un elemento de la lista en un index en específico
lista.pop(
    1
)  # Si se pone -1 elimina el último elemento de la lista,-2 el penultimo, etc.

# Remover un elemento por su valor
lista.remove(500)

# Ordenar lista de forma ascendente (Parámetro reverse=True los ordena descendente) Solo funciona con Bool y Int
lista.sort(reverse=True)

# Invierte los elementos de una lista
lista.reverse()

print(lista)

# Remover TODOS los elementos de una lista
lista.clear()
