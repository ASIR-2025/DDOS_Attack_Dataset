import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')
rx_bytes = dataset['rx_bytes'].to_numpy()
tx_bytes = dataset['tx_bytes'].to_numpy()

tx_mbs = dataset['tx_bytes'] / 1e6
rx_mbs = dataset['rx_bytes'] / 1e6

plt.figure(figsize=(15,10))
plt.plot(tx_mbs, label='tx_bytes (MB)')
plt.plot(rx_mbs, label='rx_bytes (MB)')
plt.title('Tráfico transmitido vs recibido')
plt.xlabel('Índice/tiempo)')
plt.ylabel('MB')
plt.legend()
