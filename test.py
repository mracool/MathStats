import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.figure(figsize=(8, 8))

def statistics(res, sample_range, p_k):
    stat = 0
    for i in range(0, 10):
        if p_k[i] != 0:
            stat = stat + ((res[i] - (sample_range * p_k[i])) ** 2) / (sample_range * p_k[i])
    return stat


def func_exp_dens(x, lambd):
    if x >= 0:
        return lambd * np.exp(-lambd * x)
    else:
        return 0


def func_exp(x, lambd):
    if x > 0:
        return 1 - np.exp(-lambd * x)
    else:
        return 0


with open('r2z2.csv') as sample_file:
    file_text = sample_file.read()
    file_list = file_text.split('\n')
    file_list.pop(0)
    file_list.pop(-1)
    sample = [float(element) for element in file_list]

sample_lambda = np.mean(sample)
alpha = 0.05
sample_range = len(sample)
print(sample_range)
histogram = np.histogram(sample, 10)

hist = histogram[0]
bin_edges = histogram[1]

exp_density = [func_exp_dens(bin_edges[i], sample_lambda) for i in range(len(bin_edges) - 1)]

fig, ax = plt.subplots(nrows=2, ncols=1)
plt.subplot(2, 1, 1)
plt.hist(sample, 10)

plt.subplot(2, 1, 2)
plt.plot(exp_density, 'b', label='exp density')
plt.legend()

plt.show()

exp_distribution = []
for i in range(len(bin_edges)):
    if i == 0:
        el = func_exp(bin_edges[i], sample_lambda)
    elif i == len(bin_edges):
        el = 1 - func_exp(bin_edges[i - 1], sample_lambda)
    else:
        el = func_exp(bin_edges[i], sample_lambda) - func_exp(bin_edges[i - 1], sample_lambda)
    exp_distribution.append(el)

c_critical = stats.chi2.ppf(alpha, df = sample_range - 1)
t = statistics(hist, len(sample), exp_distribution)
print(t)
print(c_critical)
p_value = 1 - (stats.chi2.cdf(t, sample_range - 1))
print(p_value)
