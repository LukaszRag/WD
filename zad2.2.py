import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('samochody.csv')
x = dane.iloc[:, 1]
labels = dane.iloc[:, 0]

plt.pie(x, labels=labels)
plt.title("Samochody zarejestrowane na terenie miasta Olsztyn")
plt.show()