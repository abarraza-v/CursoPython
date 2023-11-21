archivo_crudo = open("Apuntes\\Archivos\\texto.txt", encoding="UTF-8")

# Leer archivo completo
# archivo = archivo_crudo.read()

# Almacenar todas las lineas del txt en un array
# lineas = archivo_crudo.readlines()

# Leer una sola linea o los carácteres que desee del archivo
lineas_limitadas = archivo_crudo.readline()  # Parámetro número de caracteres

# Cerrar el archivo
archivo_crudo.close()


print(lineas_limitadas)
