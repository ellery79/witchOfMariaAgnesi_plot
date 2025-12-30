import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
agnesi = 1 / (x**2 + 1)
gaussian = np.exp(-x**2)

plt.plot(x, agnesi, label='Witch of Agnesi (1/(x^2+1))', linewidth=2)
plt.plot(x, gaussian, label='Gaussian (e^(-x^2))', linestyle='--')
plt.legend()
plt.title('Comparison: Algebraic vs Exponential Decay')
plt.grid(True)
# headless and comment out
# plt.show()
plt.savefig('agnesi_plot.png')
print("Plot saved to agnesi_plot.png")