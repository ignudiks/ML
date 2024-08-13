
mean = 0.18
var = 0.057
std = 0.238
mean_sq = mean **2


a = -(mean * (var + mean_sq - mean)) / (var)
b = (var + mean_sq - mean) * (mean - 1) / var
print("a=", a, "b=", b)
