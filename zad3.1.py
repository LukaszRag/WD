import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('wyksz.csv')
wyzsze = dane[dane["Wykształcenie"] == "wyższe"]
sred = dane[dane["Wykształcenie"] == "średnie"]
podst = dane[dane["Wykształcenie"] == "podstawowe"]
x = np.arange(0, len(wyzsze))
plt.bar(x, sred['Liczebność'], width=0.25, label="Średnie", color='green')
plt.bar(x-0.25, wyzsze['Liczebność'], width=0.25, label="Wyższe", color='blue')
plt.bar(x+0.25, podst['Liczebność'], width=0.25, label="Podstawowe", color='red')
plt.legend(loc=7)
plt.title("Wykształcenie a wiek")
plt.ticklabel_format(style='plain')
plt.xlabel('Przedział wiekowy')
plt.ylabel('Liczebność')
plt.xticks(x, sred['Wiek'])
plt.savefig("zad3.png", format='png')
plt.show()