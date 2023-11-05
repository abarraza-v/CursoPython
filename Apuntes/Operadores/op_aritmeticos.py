# ----------------------------------------

# Suma y resta (+ y -)
suma = 10 + 5
resta = 10 - 5

# Multiplicación y división (* y /)

multiplicacion = 10 * 5
division = 10 / 5  # Siempre devuelve un datatype FLOAT (en este caso 2.0 en ves de 2)

# Potenciación (exponente) (**)
exponente = 10**5

# División baja (//)
division_baja = (
    10 // 5
)  # Redondea entero hacia abajo ignorando el decimal (Siempre devuelve un Int)

# Resto de división o Módulo (%)
resto = 10 % 5

# ----------------------------------------

# type(variable) es una función que nos devuelve el tipo de dato de la variable que envíamos.
tipo_de_dato = type(division)

print(tipo_de_dato)
