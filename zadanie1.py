import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lista = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(lista, header=0)
dzieci = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(dzieci)
dzieci.plot.bar()
plt.show()




