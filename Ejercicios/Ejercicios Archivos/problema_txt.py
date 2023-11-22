nombres = ["ramón", "roberto", "alejandro", "pangasio"]
apellidos = ["valdés", "valencia", "peralta", "rique"]

# Registrar esta información en un TXT de forma óptima

with open(
    "Ejercicios\\Ejercicios Archivos\\problema.txt", "w", encoding="UTF-8"
) as archivo:
    archivo.writelines("\n")
    [
        archivo.writelines(
            f"\n-------\n Nombre: {nombre} \n Apellido: {apellido}\n-------"
        )
        for nombre, apellido in zip(nombres, apellidos)
    ]
