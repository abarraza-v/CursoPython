# Creando función simple


def despedirse():
    print("adiós")


# Creando función con parámetros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titán"
    else:
        adjetivo = "crack"
    print(f"Hola {nombre}, cómo andas {adjetivo}, ¿Todo bien?")


saludar("Tomás", "hombre")


# Creando función que retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_string = str(num)
    num = int(num_string[0])
    char1 = num - 2
    char2 = num
    char3 = num - 5
    contraseña = f"{chars[char1]}{chars[char2]}{chars[char3]}{num * 2}"

    return contraseña, num


# Desempaquetando la tupla que nos retorna la función
nueva_contraseña, primer_numero = crear_contraseña_random(9)

# Mostrando los datos obtenidos
print(nueva_contraseña)
print(primer_numero)
