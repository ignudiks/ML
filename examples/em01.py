from scipy.stats import norm
import numpy as np


def emc(mean1, mean2, sd1, sd2, prior1, prior2):
  posterior1 = prior1 * norm.pdf(X, mean1, sd1)
  posterior2 = prior2 * norm.pdf(X, mean2, sd2)
  total = posterior1 + posterior2

  w1 = posterior1 / total
  w2 = posterior2 / total

  mean1 = np.sum(w1 * X) / np.sum(w1)
  mean2 = np.sum(w2 * X) / np.sum(w2)
  sd1 = np.sqrt(np.sum(w1 * (X - mean1) ** 2) / np.sum(w1))
  sd2 = np.sqrt(np.sum(w2 * (X - mean2) ** 2) / np.sum(w2))
  prior1 = np.mean(w1)
  prior2 = np.mean(w2)

  return (mean1, mean2, sd1, sd2, prior1, prior2)


def fmt(X):
    return ["{:.15f}".format(x) for x in X]

X = [1.0, 1.3, 2.2, 2.6, 2.8, 5.0, 7.3, 7.4, 7.5, 7.7, 7.9]
mean1, sd1, prior1 = 6.63, 1, 0.5
mean2, sd2, prior2 = 7.57, 1, 0.5

for _ in range(5):  
  (mean1, mean2, sd1, sd2, prior1, prior2) = emc(mean1, mean2, sd1, sd2, prior1, prior2)
  print(mean1)
  print(mean2)
  print(sd1**2)
  print(sd2**2)
  print(prior1)
  print(prior2)
  print("-----------------------------")
