import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')
datos_agrupados = dataset.groupby('Protocol')['flows'].sum()

# Obtener nombres de protocolos y valores
protocolos = datos_agrupados.index
cantidades = datos_agrupados.values

plt.figure(figsize=(12, 6))
plt.bar(protocolos, cantidades, color='steelblue')

# Títulos y etiquetas
plt.title('Cantidad de Flujos por Protocolo')
plt.xlabel('Protocolo')
plt.ylabel('Cantidad de Flujos')
plt.xticks(rotation=45)  # rotar etiquetas si hay muchas

plt.grid()
plt.show()
