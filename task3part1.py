import pandas as pd

file_name = 'r3z1.csv'

data = pd.read_csv(file_name)

print( data.mean())
sample_var = data.var