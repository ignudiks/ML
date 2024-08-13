import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x = 4.5
scale = 0.5
loc_values = np.linspace(1.5, 7.5, 7)
for loc in loc_values:
    print(f"{loc:.1f}", ":", f"{norm.pdf(x, loc, scale):.4f}")

# plotting the graph
loc_values = np.linspace(1.5, 7.5, 10000)
likelihood_values = [norm.pdf(x, loc, scale) for loc in loc_values]
plt.plot(loc_values, likelihood_values)
plt.show()