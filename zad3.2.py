import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('sklepy.csv', index_col=0)
dane2016 = dane[dane.Rok == 2016]
print(dane2016)

x = np.arange(0, len(dane2016))
plt.bar(x, dane2016['Liczba obiektów'])
plt.title("Rodzaje sklepów w Olsztynie w 2016 r.")
plt.xticks(x, dane2016.index)
plt.show()