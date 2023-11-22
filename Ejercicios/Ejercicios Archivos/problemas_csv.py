# Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("Ejercicios\\Ejercicios Archivos\\problema.csv")

# Convertir a string los valores de una columna
df["Edad"] = df["Edad"].astype(str)

print(type(df["Edad"][0]))

# Reemplazando los datos "Alejandro" por "Maestro"
df["Apellido"].replace("B", "Barraza", inplace=True)

print(df)

# Eliminando las filas con datos faltantes.
df = df.dropna()

# Eliminando las columnas con datos faltantes.
# df = df.dropna(axis=1)

# Eliminando los datos repetidos.
df = df.drop_duplicates()
print(df)

# Creando un CSV con el dataframe resultante
df.to_csv("Ejercicios\\Ejercicios Archivos\\problema_resuelto.csv")
