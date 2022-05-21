import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x= np.arange(0,10,0.01)
y1=np.log(x)
y2=np.exp(x)

fig, ax1 = plt.subplots()
ax1.plot(x,y1, color="green", label="y=ln(x)")
ax2= ax1.twinx()
ax2.plot(x,y2, color="blue", linestyle="dashed", label="y=exp(x)")
ax1.legend(loc=2)
ax2.legend(loc=4)
plt.title("tytul")
ax1.tick_params("y",colors="green")
ax2.tick_params("y",colors="blue")
ax1.set_ylabel("ax1")
ax2.set_ylabel("ax2")


plt.show()