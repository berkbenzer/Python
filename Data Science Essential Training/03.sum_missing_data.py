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

sum_df=df_obj.isnull().sum()
print(sum_df)




0    3
1    0
2    0
3    0
4    0
5    4
