import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_excel("mieszkania1.xlsx")

dane1 = dane[dane['Formy budownictwa'] == "indywidualne"]
dane2 = dane[dane['Formy budownictwa'] == "spółdzielcze"]
dane3 = dane[dane['Formy budownictwa'] == "komunalne"]
x = np.arange(0, len(dane1))
plt.bar(x, dane1['Wartość'], width=0.25, label="indywidualne")
plt.bar(x-0.25, dane2['Wartość'], width=0.25, label='spółdzielcze')
plt.bar(x+0.25, dane3['Wartość'], width=0.25, label='komunalne')
plt.xticks(x, dane1["Rok"])
plt.title("Ilość różnych form budownictwa w latach 2015-2018")
plt.xlabel("Rok")
plt.ylabel("Ilość")
plt.legend(loc=7)
plt.annotate('165926', [-0.5, 68000])
plt.savefig("zad2.pdf", format="pdf")
plt.show()