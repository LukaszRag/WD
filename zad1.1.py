import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(-5, 10, step=0.01)
y = (4-x+x**3)/(6+x-4*x**2+x**3)

plt.plot(x, y, color='lightblue')
plt.ylim(-30, 30)

#asymptota pozioma
av = np.ones(len(x))
plt.plot(x, av, linestyle='dashed', color='red')

#asymptoty pionowe
x1 = [-1, -1]
y1 = [-30, 30]
plt.plot(x1, y1, linestyle='dashed', color='orange')

x2 = [2, 2]
plt.plot(x2, y1, linestyle='dashed', color='lime')

x3 = [3, 3]
plt.plot(x3, y1, linestyle='dashed', color='purple')

#stylowanie
plt.title("Wykres funckji")
plt.legend(['f(x)', 'y=1', 'x=-1', 'x=2', 'x=3'])
plt.savefig("zad1.pdf", format="pdf")
plt.show()