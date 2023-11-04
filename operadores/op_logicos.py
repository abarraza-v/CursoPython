# AND Todos los valores tienen que ser True.

Resultado = True & True  # Devuelve True
Resultado2 = False & True  # Devuelve False
Resultado3 = True & False  # Devuelve False
Resultado4 = False & False  # Devuelve False

# OR Uno de los valores tiene que ser True.

Resultado5 = True | True  # Devuelve True
Resultado6 = False | True  # Devuelve True
Resultado7 = True | False  # Devuelve True
Resultado8 = False | False  # Devuelve False

# NOT Invierte el valor. Si es True, ahora pasa a ser False y viceversa

Resultado9 = not True  # Devuelve False
Resultado10 = not False  # Devuelve True

Resultado11 = not 2 == 2  # Efectivamente 2 es igual a 2, por eso devuelve False.

print(Resultado11)
