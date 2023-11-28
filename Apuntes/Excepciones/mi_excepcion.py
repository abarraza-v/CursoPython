class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")


# Lanzando mi propia excepción
# raise MiExcepcion("Que tonto, dividiste por cero")

# Manejándola
try:
    raise MiExcepcion("Jaaaaa, te equivocaste")
except:
    print("Cómo vas a cometer ese error?")
