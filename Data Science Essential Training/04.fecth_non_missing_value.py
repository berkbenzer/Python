import numpy as np
import pandas as pd

from pandas import Series, DataFrame


#Figuring out what data is missing
#nan is library find the missing values

missing = np.nan
series_obj = Series(['row1','row2',missing,'row5','row6',missing,'row8'])

np.random.seed(25)
df_obj = DataFrame(np.random.rand(36).reshape(6,6))


df_obj.ix[3:5,0] = missing
df_obj.ix[1:4,5] = missing


df_no_nan = df_obj.dropna()
print(df_no_nan)


#          0         1         2         3       4         5
#0  0.870124  0.582277  0.278839  0.185911  0.4111  0.117376
