ingresos_mensuales = 10001
gastos_mensuales = 1500
balance_final = ingresos_mensuales - gastos_mensuales

if ingresos_mensuales > 10000:
    print("Con el dinero que ganas DEBERÍAS estár bien en cualquier país")
    if balance_final < 0:
        print(
            "Tus gastos son tan altos que estás en deficit, así que ponte a pagar deudas."
        )
    elif balance_final > 1000:
        print("Vas muy bien porque estás generando una buena cantidad de ahorros")
    else:
        print(
            "Estás gastando demasiado así que quizá no puedas vivir tan cómodamente como pensabas"
        )
elif ingresos_mensuales > 500:
    print("Con el dinero que ganas DEBERÍAS estár bien en Argentina")
elif ingresos_mensuales > 200:
    print("Con el dinero que ganas DEBERÍAS vivir bien en Venezuela")
else:
    print("Eres pobre")
