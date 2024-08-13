import numpy as np
from scipy.stats import binom
from scipy.stats import beta
import matplotlib.pyplot as plt


n, k = 1, 0
a, b = 0.5, 0.5
rv = beta(a, b)
sample_b = 3

p_c = 0.5

p_p_values = [0.2, 0.006, 0.07, 0.089, 0.023, 0.001, 0.124, 0.001, 0.032, 0.044]
r_numbers = [0.372, 0.572, 0.216, 0.364, 0.098, 0.175, 0.507, 0.372, 0.572, 0.216]


p_c_posterior = rv.pdf(p_c) * binom.pmf(k, n, p_c)
p_c_sample_a = (sample_b * p_c) / (1 - p_c)

for p_p in p_p_values:
    p_p_posterior = rv.pdf(p_p) * binom.pmf(k, n, p_p)
    p_p_sample_a = (sample_b * p_p) / (1 - p_p)
    ratio = p_p_posterior / p_c_posterior
    CF = beta(p_p_sample_a, sample_b).pdf(p_c) / beta(p_c_sample_a, sample_b).pdf(p_p)
    M = min(ratio * CF, 1)
    r = r_numbers.pop(0)

    print(
        round(p_c, 3),
        "\t",
        round(p_c_posterior, 3),
        "\t",
        round(p_c_sample_a, 3),
        "\t",
        sample_b,
        "\t",
        round(p_p, 3),
        "\t",
        round(p_p_posterior, 3),
        "\t",
        round(p_p_sample_a, 3),
        "\t",
        sample_b,
        "\t",
        round(ratio, 3),
        "\t",
        round(CF, 3),
        "\t",
        round(M, 3),
        "\t",
        r,
    )

    if M > r:
        p_c = p_p
        p_c_posterior = p_p_posterior
        p_c_sample_a = p_p_sample_a
        print("Yes")
    else:
        print("No")
