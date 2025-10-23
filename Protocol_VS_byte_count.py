import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')
grupo = dataset.groupby("Protocol")["bytecount"].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(grupo["Protocol"].astype(str), grupo["bytecount"])
plt.xlabel("Protocolos")
plt.ylabel("Cantidad de Bytes")
plt.title("Cantidad de bytes por Protocolo")
plt.xticks(rotation=45)
# Ajustar márgenes
plt.tight_layout()
plt.show()
