import pandas as pd
from pandas import DataFrame
import numpy
import seaborn as sns
import matplotlib.pyplot as plt


def func_exp(x, lambd):
    if x > 0:
        return 1 - numpy.exp(-lambd*x)
    else:
        return 0

def statictics(res, sample_range, p_k):
    stat = 0
    for i in range(0,10):
      stat = stat +((res[i]-(sample_range*p_k[i]))**2)/(sample_range*p_k[i])
    return stat

file_name = 'r2z2.csv'

data = pd.read_csv(file_name)
df = DataFrame(data, columns=['X'])
lists_of_data = df.values.tolist()
sample_range = data.max()-data.min()
frequency = [[0] * i for i in range(12)]

#hist
af = sns.distplot(data, bins=10) #вероятностная гистограмма
plt.show()

ax = data.plot.hist(bins=10)
plt.show()

lambd = (data.mean())
# print(lambd)

s = pd.Series([k[0] for k in lists_of_data])
bins = numpy.arange((s.min()), (s.max()), ((s.max()) - (s.min()))/10)
print(bins)
# print((s.min()), (s.max()))
res = s.groupby(pd.cut(s, bins=bins, right=False)).size()
hist_list = res.to_list()
hist_list = [0]+hist_list+[0]
print((hist_list))
# hist_list = [2, 2, 11, 10, 12, 11, 15, 10, 7, 4]

p_k = [[0] * i for i in range(12)]
p_k[0] = func_exp(bins[0], lambd)
p_k[11] = 1 - func_exp(bins[11], lambd)
print(p_k)
#calculating Pk's
for i in range(0,11):
    p_k[i] = func_exp(bins[i], lambd) - func_exp(bins[i-1], lambd)

print(bins)
print((p_k))
print((statictics(hist_list, sample_range, p_k)))
# for i in p_k:
#     print(i*sample_range)

