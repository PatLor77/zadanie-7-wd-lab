import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lista = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(lista, header=0)
dzieci = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(dzieci)
dzieci.plot()
plt.xticks(np.arange(2000, 2018, step=1))
plt.xticks(rotation=90)
plt.show()





