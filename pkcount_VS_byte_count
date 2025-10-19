import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')
plt.figure(figsize=(10, 6))
plt.scatter(x = dataset["pktcount"], y = dataset["bytecount"], color='red')
plt.title('Comparación de PK y Bytes')
plt.xlabel('Pktcount')
plt.ylabel('Bytes (MB)')
plt.grid(True)
plt.show()
