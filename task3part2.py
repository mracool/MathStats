import pandas as pd
from scipy import stats

def lower_confidence_limit(n, s, alpha):
    func = (s*(n-1))/stats.chi2.ppf(alpha, df = n - 1)
    return func

file_name = 'r3z2.csv'

data = pd.read_csv(file_name)

alpha = 0.99
s_range = int(data.size)
s_var = int(data.var())
print(s_range, s_var, alpha)
# c = lower_confidence_limit(s_range, s_var, alpha)
print(lower_confidence_limit(s_range, s_var, alpha))



