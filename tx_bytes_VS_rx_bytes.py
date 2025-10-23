import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
rx_bytes = dataset['rx_bytes'].to_numpy()
tx_bytes = dataset['tx_bytes'].to_numpy()

dataset = pd.read_csv('dataset_sdn_normal.csv')
tx_mbs = dataset['tx_bytes'] / 1e6
rx_mbs = dataset['rx_bytes'] / 1e6

plt.figure(figsize=(12,10))
plt.plot(tx_mbs, label='tx_bytes (MB)',color='red')
plt.plot(rx_mbs, label='rx_bytes (MB)')
plt.title('Tráfico transmitido vs recibido')
plt.xlabel('Índice/tiempo')
plt.ylabel('MB')
plt.legend()

##OTROS DATOS
tx_bytes_mean = tx_bytes.mean()
tx_bytes_max = tx_bytes.max()
tx_bytes_min= tx_bytes.min()
print('Total de tx_bytes enviados:', tx_bytes_sum)
print('Media de tx_bytes:', tx_bytes_mean)
print('Maximo de tx_bytes', tx_bytes_max)
print('Minimo de tx_bytes', tx_bytes_min)

rx_bytes = dataset['rx_bytes'].to_numpy()
rx_bytes_sum = rx_bytes.sum()
rx_bytes_mean = rx_bytes.mean()
rx_bytes_max = rx_bytes.max()
rx_bytes_min= rx_bytes.min()
print('Total de rx_bytes enviados:', rx_bytes_sum)
print('Media de rx_bytes:', rx_bytes_mean)
print('Maximo de rx_bytes', rx_bytes_max)
print('Minimo de rx_bytes', rx_bytes_min)
