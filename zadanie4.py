import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lista = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(lista, header=0)
dane = pd.read_csv("zamowienia.csv",sep=';')
print(dane[['Sprzedawca','Utarg']])
suma =  dane.groupby('Sprzedawca').agg({'Utarg':['sum']})
suma.plot.bar()
plt.xticks(rotation=0)
plt.show()



