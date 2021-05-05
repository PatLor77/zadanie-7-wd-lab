import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
nazwiska = df['Sprzedawca']
nazwiska= nazwiska.unique()
print(pd.Series(nazwiska))
print()
df['Utarg'] = df['Utarg'].astype(float)
utargi = (df.sort_values(by='Utarg', ascending=False).head(5))
print(utargi['Utarg'])
print()
print(df.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))
print()
print(df.groupby('Kraj').agg({'Kraj':['count']}))
print()
df['Data zamowienia'] = df['Data zamowienia'].astype('datetime64[ns]')
polacy = (df[(df.Kraj == 'Polska') & (df['Data zamowienia'].dt.year == 2005)])
print(polacy.groupby('Kraj').agg({'Utarg':['sum']}))
print()
czwarty = df[(df['Data zamowienia'].dt.year == 2004)]
print(czwarty['Utarg'].mean())
print()
czwarty = df[(df['Data zamowienia'].dt.year == 2004)]
piaty = df[(df['Data zamowienia'].dt.year == 2005)]
czwarty.to_csv('zamowienia_2004.csv', index=False)
piaty.to_csv('zamowienia_2005.csv', index=False)
