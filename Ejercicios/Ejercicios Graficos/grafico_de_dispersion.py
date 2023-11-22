import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Ejercicios\Ejercicios Graficos\coords.csv")

# Creando el gráfico
sns.scatterplot(x="tiempo", y="dinero", data=df)

plt.show()
