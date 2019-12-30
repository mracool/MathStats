import pandas as pd
from scipy import stats


def lower_confidence_bound(n, s, alpha):
    s = s * (n - 1) / (n)
    # ask if the variance right, cause it's unbaised here
    func = (s * n) / (stats.chi2.ppf(1 - alpha, df=n - 1))
    return func

file_name = 'r3z2.csv'

data = pd.read_csv(file_name)

alpha = 1 - (0.99)
print(alpha)
s_range = int(data.size)
s_var = float(data.var())
print(s_range, s_var, alpha)
print(lower_confidence_bound(s_range, s_var, alpha))
