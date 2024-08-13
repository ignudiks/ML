import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

x = 2
n = 3
p_values = np.linspace(0, 1, 11)
for p in p_values:
    print(f"{p:.1f}", ":", f"{binom.pmf(x, n, p):.3f}")

# plotting the graph
p_values = np.linspace(0, 1, 10000)
likelihood_values = [binom.pmf(x, n, p) for p in p_values]
plt.plot(p_values, likelihood_values)
plt.show()