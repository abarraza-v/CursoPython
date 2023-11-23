# Creando función que suma números
def sumar_dos():
    # Iniciando un bucle
    while True:
        # Pidiendo números
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # Intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        # Si lanza una excepción, se ejecuta este bloque de código
        except ValueError as e:
            print(f"ERROR: {e}")
            print("Te pedí un número no letras, genio")
        # Si todo salió bien, terminamos el bucle
        else:
            break
        finally:
            print("Manejo de excepción finalizado")
    return resultado


print(sumar_dos())
