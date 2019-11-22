import numpy as np
import pandas as pd

from pandas import Series, DataFrame

data_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})


print(data_obj)

   # column 1 column 2 column 3
# 0         1        a        A
# 1         1        a        A
# 2         2        b        B
# 3         2        b        B
# 4         3        c        C
# 5         3        c        C
# 6         3        c        C

print(data_obj.duplicated())

# 0    False
# 1     True
# 2    False
# 3     True
# 4    False
# 5     True
# 6     True

print(data_obj.drop_duplicates())

   # column 1 column 2 column 3
# 0         1        a        A
# 2         2        b        B
# 4         3        c        C
     
