import pandas as pd
import numpy as np

from pandas import Series, DataFrame
series_obj = Series(np.arange(8), index=['row1','row2','row3','row4','row5','row6','row7','row8'] )

# print(series_obj)
# row1    0
# row2    1
# row3    2
# row4    3
# row5    4
# row6    5
# row7    6
# row8    7
# dtype: int32

#print(series_obj[[0,4]])
# row1    0
# row5    4
# dtype: int32

np.random.seed(25)
DF_OBJ= DataFrame(np.random.rand(36). reshape((6,6)), index=['row1','row2','row3','row4','row5','row6'] ,
                  columns=['column1','column2','column3','column4','column5','column6'])

print(DF_OBJ)
       # column1   column2   column3   column4   column5   column6
# row1  0.870124  0.582277  0.278839  0.185911  0.411100  0.117376
# row2  0.684969  0.437611  0.556229  0.367080  0.402366  0.113041
# row3  0.447031  0.585445  0.161985  0.520719  0.326051  0.699186
# row4  0.366395  0.836375  0.481343  0.516502  0.383048  0.997541
# row5  0.514244  0.559053  0.034450  0.719930  0.421004  0.436935
# row6  0.281701  0.900274  0.669612  0.456069  0.289804  0.525819

print(DF_OBJ.ix[['row2','row5'],['column5','column2']])

# row2  0.402366  0.437611
# row5  0.421004  0.559053



#DATA SLICING
print(series_obj['row3':'row7'])

row3    2
row4    3
row5    4
row6    5
row7    6
dtype: int32


#FILTERING WITH SCALARS
print(DF_OBJ < .2)
 # column1  column2  column3  column4  column5  column6
# row1    False    False    False     True    False     True
# row2    False    False    False    False    False     True
# row3    False    False     True    False    False    False
# row4    False    False    False    False    False    False
# row5    False    False     True    False    False    False
# row6    False    False    False    False    False    False



series_obj['row1','row5','row8']= 8
print(series_obj)

# row1    8
# row2    1
# row3    2
# row4    3
# row5    8
# row6    5
# row7    6
# row8    8
# dtype: int32



