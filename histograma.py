import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')

plt.hist(dataset['pktrate'], bins=30, color='skyblue')
plt.title('Histograma de pktrate')
plt.xlabel('pktrate')
plt.ylabel('Frecuencia')
plt.show()
