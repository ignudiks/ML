import numpy as np
from scipy.stats import poisson
from scipy.stats import gamma
import matplotlib.pyplot as plt


n, k = 1, 5
a, b = 2.1, 1

mu_values = [3.1, 4.2, 2.36, 2.637,2.306,2.435, 2.674,2.166,2.692,2.035,2.616]


for mu in mu_values:
    print(mu)
    prior = gamma.pdf(mu, a=a, scale = 1/b)
    print(prior)
    likelihood = poisson.pmf(k, mu)
    print(likelihood)
    posterior = prior * likelihood
    print(posterior)

