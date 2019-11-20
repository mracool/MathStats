import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import ecdf
from statsmodels.distributions import ECDF
file_name = 'data.csv'

data = pd.read_csv(file_name)
# print('This is data:')
# print(data) #sample

#Task 1.1
sample_volume = data.size
print('This is data volume:')
print(sample_volume) #sample volume

sample_min = data.min()
print('This is data minimum:')
print(sample_min)

sample_max = data.max()
print('This is data maximum:')
print(sample_max)

sample_range = sample_max - sample_min
print('This is data range:')
print(sample_range)

sample_mean = data.mean()
print('This is data mean:')
print(sample_mean)

sample_unb_variance = data.var()
print('This is data unbiased variance:')
print(sample_unb_variance)

sample_variance = ((sample_volume-1)/sample_volume)*data.var()
print('This is data variance:')
print(sample_variance)

sample_skewness = data.skew()
print('This is data skewness:')
print(sample_skewness)

sample_median = data.median()
print('This is data mediane:')
print(sample_median)

#interquartile latitude
q1 = data.quantile(0.25)
q2 = data.quantile(0.75)
sample_iqr = q2-q1
print('This is data interquartile latitude:')
print(sample_iqr)

#Task 1.2
# ax = data.plot.hist(bins=10) частотная гистограмма
af = sns.distplot(data, bins=10) #вероятностная гистограмма
plt.show()
print('This is data mode') #mode of sample
print(data.mode())

#Task 1.3
#trying to find out distribution function
file = ECDF(data['X'])
data['Y'] = data['X'].apply(file)
sns.lineplot(data['X'], data['Y'], drawstyle = 'steps-pre')
plt.show()

