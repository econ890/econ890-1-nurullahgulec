# This is exercise for matplotlib lecture.

# Nurullah Gulec 5 August 2020

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)

for theta in np.linspace(0,2,10) :
    y = np.cos(np.pi * theta * x) * np.exp(-x)
    ax.plot(x, y, linewidth=2, alpha=0.6)

ax.legend()
plt.show()
