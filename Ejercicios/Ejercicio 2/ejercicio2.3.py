def fibonacci(num):
    a, b = 0, 1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num:
            return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            temp = b
            b = a + b
            a = temp
            # con desempaquetado
            # a, b = b, a + b


resultado = fibonacci(20)
print(resultado)
