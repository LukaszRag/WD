import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_excel("turystyka1.xlsx", header=None)
dane2 = dane.transpose()
dane3 = dane2.rename({0: 'Kategoria', 1: 'Rok', 2: 'Ilość'}, axis='columns')

dane_ax1 = dane3[dane3['Rok'] == '2018']
dane_ax2 = dane3[dane3['Rok'] == '2019']
labels = dane_ax1.iloc[:, 0]

plt.pie(dane_ax1['Ilość'], labels=labels, autopct='%1.0f%%', explode=[0, 0, 0.1, 0, 0])
plt.title("Ilość poszczególnych kategorii hoteli w roku 2018")
plt.savefig("zad3a.jpg", format='jpg')
plt.show()

