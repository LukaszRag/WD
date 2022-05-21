import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sport.xlsx", header=None)
x = df.iloc[:, 1]
etykiety = df.iloc[:, 0]
plt.pie(x, labels=etykiety, autopct='%1.0f%%', explode=(0.1,0,0,0,0,0))
plt.annotate('Dawid Końpa', [-1.2, 1])
plt.title("Popularność sportów w grupie nastolatków")
plt.savefig("zad2.jpg", format='jpg')
plt.show()