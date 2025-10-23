import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')
# Calcular estadísticos por protocolo
duracion_stats = dataset.groupby('Protocol')['dur'].agg(['mean', 'max', 'min']).sort_index()

# Crear gráfico de líneas
plt.figure(figsize=(10,6))
plt.plot(duracion_stats.index, duracion_stats['mean'], marker='o', color='blue', linewidth=2, label='Promedio')
plt.plot(duracion_stats.index, duracion_stats['max'], marker='^', color='red', linestyle='--', label='Máximo')
plt.plot(duracion_stats.index, duracion_stats['min'], marker='v', color='green', linestyle='--', label='Mínimo')

# Etiquetas y estilo
plt.title('Duración de Flujos por Protocolo (mínimo, promedio y máximo)', fontsize=14)
plt.xlabel('Protocolo')
plt.ylabel('Duración (segundos)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
