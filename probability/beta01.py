import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

a, b = 0.5, 1.5
p_values = np.linspace(0, 1, 11)

# plotting the graph
x_values = np.linspace(0, 1, 10000)
y_values = [beta.pdf(x, a, b) for x in x_values]
print(y_values[0])
plt.plot(x_values, y_values)
plt.show()