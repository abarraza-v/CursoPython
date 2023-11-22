import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Ejercicios\Ejercicios Graficos\\renta.csv")

# Creando el gráfico
sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos = df["ingresos"].sum()

print(f" El total de ingresos es de: ${total_ingresos} USD")

plt.show()
