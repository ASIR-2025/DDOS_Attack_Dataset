import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('dataset_sdn_normal.csv')
plt.plot(dataset["dt"], dataset["tot_kbps"], color='blue', marker='o')
plt.title('Dt vs kbps')
plt.xlabel('DT')
plt.ylabel('Total de kbps')
plt.grid(True)
plt.show()
