import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Ejercicios\Ejercicios Graficos\pedos.csv")

# Creando el gráfico
sns.lineplot(x="fecha", y="pedos", data=df)

# Creando un punto en el momento de más pedos
plt.plot("15-11-23", 17, "o")

plt.show()
