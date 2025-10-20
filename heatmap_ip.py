import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')

data = pd.crosstab(dataset["src"], dataset["dst"])

plt.figure(figsize=(6, 5))
sns.heatmap(data, annot=True, cmap='viridis')  # annot=True para mostrar los números
plt.title('Heatmap')
plt.xlabel('dst')
plt.ylabel('src')
plt.show()
