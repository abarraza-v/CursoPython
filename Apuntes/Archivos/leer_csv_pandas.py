import pandas as pd

# Parámetro names=["Name", "Lastname", "Age"]
df = pd.read_csv("Apuntes\\Archivos\\datos.csv")
df2 = pd.read_csv("Apuntes\\Archivos\\datos.csv")

# Obteniendo datos de la columna nombre
nombres = df["Edad"]

# Ordenando el dataframe por edad
df_ascendente = df.sort_values("Edad")
df_descendente = df.sort_values("Edad", ascending=False)

# Concatenando 2 dataframes
df_concatenado = pd.concat([df, df2])

# Accediendo a las primeras 3 filas con head()
primeras_filas = df_concatenado.head(3)

# Accediendo a las últimas 3 filas con tail()
primeras_filas = df_concatenado.tail(3)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

# Obteniendo estadística del dataframe.
df_info = df.describe()

# Accediendo a un elemento específico del df con loc
elemento_especifico_loc = df.loc[2, "Edad"]

# Accediendo a un elemento específico del df con índice loc
elemento_especifico_iloc = df.iloc[2, 2]

# Accediendo a todos los apellidos con loc
apellidos = df.loc[:, "Apellido"]

# Accediendo a todos los apellidos con iloc
apellidos = df.iloc[:, 1]

# Accediendo a fila 3 con loc
fila_3 = df.loc[2, :]

# Accediendo a la fila 3 con iloc
fila_3 = df.loc[2, :]

# Accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["Edad"] > 30, :]

# Accediendo a filas con edad menor que 30
menor_que_30 = df.loc[df["Edad"] < 30, :]
print(mayor_que_30)
