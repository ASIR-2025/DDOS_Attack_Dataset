import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')

# Crear gráfico scatter
plt.figure(figsize=(7, 6))
plt.scatter(dataset["dst"], dataset["src"], alpha=0.7)
# Etiquetas y título
plt.title("Relación entre src y dst (Scatter)")
plt.xlabel("dst")
plt.ylabel("src")
plt.colorbar(label="Frecuencia")
plt.show()
