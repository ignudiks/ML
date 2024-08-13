import numpy as np
from scipy.stats import binom
from scipy.stats import beta
import matplotlib.pyplot as plt

n, k = 1, 0
prior = beta(0.5, 0.5)
sample_b = 3
p_c = 0.5
p_c_posterior = prior.pdf(p_c) * binom.pmf(k, n, p_c)
p_c_sample_a = (sample_b * p_c) / (1 - p_c)

p_values = []
for inx in range(10000):
    p_p = np.random.beta(p_c_sample_a, sample_b)
    p_p_posterior: float
    try:
        p_p_posterior = prior.pdf(p_p) * binom.pmf(k, n, p_p)
    except OverflowError as oe:
        continue

    if inx > 1000:
        p_values.append(p_c)

    p_p_sample_a = (sample_b * p_p) / (1 - p_p)
    ratio = p_p_posterior / p_c_posterior
    CF = beta(p_p_sample_a, sample_b).pdf(p_c) / beta(p_c_sample_a, sample_b).pdf(p_p)
    M = min(ratio * CF, 1)
    r = np.random.uniform(low=0.0, high=1.0)

    if M > r:
        p_c = p_p
        p_c_posterior = p_p_posterior
        p_c_sample_a = p_p_sample_a

array = np.array(p_values)
mean,std, min, max = np.mean(array), np.std(array), np.min(array), np.max(array)
mean_sq, var = mean**2 , std**2

print(mean, var , std , min, max)
a = -(mean * (var + mean_sq - mean)) / (var)
b = (var + mean_sq - mean) * (mean - 1) / var
print("a=", a, "b=", b)
