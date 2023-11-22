import csv

with open("Apuntes\\Archivos\\datos.csv") as archivo:
    datos = csv.reader(archivo)
    print(datos)
    for row in datos:
        print(row)
