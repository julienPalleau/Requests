import pandas as pd

df = pd.DataFrame({'team': ['Mavs', 'Lakers', 'Spurs', 'Cavs'],
                   'name': ['Dirk', 'Kobe', 'Tim', 'Lebron'],
                   'rebounds': [11, 7, 14, 7],
                   'points': [26, 31, 22, 29]})

print(df)
df = df[df.rebounds != 7]
print(df)