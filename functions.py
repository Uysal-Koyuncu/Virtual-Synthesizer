import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,44100)
y = np.sin(x * 261 * 2 * np.pi)
plt.plot(x[:5000],y[:5000])
plt.show()