import pandas as pd
from pandas import DataFrame
from scipy import stats


def statistics(mean, var, n):
    # function of statistics
    T = (mean/(var)**(1/2))*((n-1)**(1/2))
    return T


alpha = 0.01
file_name = 'r2z1.csv'
data = pd.read_csv(file_name)
df = DataFrame(data, columns=['X', 'Y'])
lists_of_data = df.values.tolist()
x_sample = [[0] * i for i in range(len(lists_of_data))]
y_sample = [[0] * i for i in range(len(lists_of_data))]
u_sample = [[0] * i for i in range(len(lists_of_data))]
for i in range(0, len(lists_of_data)):
    x_sample[i] = lists_of_data[i][0]
    y_sample[i] = lists_of_data[i][1]
print(x_sample)
print(y_sample)

for i in range(0, len(lists_of_data)):
    u_sample[i] = (x_sample[i]-y_sample[i])
print(u_sample)

sample_volume = pd.DataFrame(u_sample).size
u_mean = pd.DataFrame(u_sample).mean()
print(sample_volume)
# new sample's unbiased variance
u_var = ((sample_volume-1)/sample_volume)*(pd.DataFrame(u_sample).var())
print(u_var)

#µ > m0 {T : T > Cкрит}
# critical const: Fstud−1(1 − α | n − 1)
c_critical = stats.t.ppf(1-alpha, df = sample_volume - 1)
# p-value^  1 − Fstud(t| n − 1)
t = statistics(u_mean, u_var, sample_volume)
p_value = 1 - (stats.t.cdf(t, sample_volume - 1))
print("criterii")
print(c_critical)
print(p_value)
print("statistics: ")
print(statistics(u_mean, u_var, sample_volume))

