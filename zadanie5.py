import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
print(df[df['Liczba'] < 1000])
print()
print(df[df.Imie == 'DANIEL'])
print()
print(sum(df['Liczba']))
print()
print(sum(df['Liczba'] & ((df.Rok) > 2004) & ((df.Rok) < 2011) ))
print()
print(sum(df['Liczba'] & ((df.Plec) == 'M') & ((df.Rok) == 2000) ))
print()
d = df[(df.Plec == 'K')]
m = df[(df.Plec == 'M')]
print(df.Imie[df.Liczba == max(m.Liczba)])
print(df.Imie[df.Liczba == max(d.Liczba)])
grupa = df.groupby(['Rok', 'Plec']).agg({'Liczba':['max']})
print(grupa)
