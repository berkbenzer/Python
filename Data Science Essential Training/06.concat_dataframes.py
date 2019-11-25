import numpy as np
import pandas as pd

from pandas import Series, DataFrame


df_obj = pd.DataFrame(np.arange(36).reshape(6,6))
print(df_obj)


    # 0   1   2   3   4   5
# 0   0   1   2   3   4   5
# 1   6   7   8   9  10  11
# 2  12  13  14  15  16  17
# 3  18  19  20  21  22  23
# 4  24  25  26  27  28  29
# 5  30  31  32  33  34  35

df_obj2 = pd.DataFrame(np.arange(15).reshape(5,3))
print(df_obj2)

    # 0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14

#joins data from seperate sources

print(pd.concat([df_obj,df_obj2], axis= 1))

    # 0   1   2   3   4   5     0     1     2
# 0   0   1   2   3   4   5   0.0   1.0   2.0
# 1   6   7   8   9  10  11   3.0   4.0   5.0
# 2  12  13  14  15  16  17   6.0   7.0   8.0
# 3  18  19  20  21  22  23   9.0  10.0  11.0
# 4  24  25  26  27  28  29  12.0  13.0  14.0
# 5  30  31  32  33  34  35   NaN   NaN   NaN



print(pd.concat([df_obj,df_obj2]))


    # 0   1   2     3     4     5
# 0   0   1   2   3.0   4.0   5.0
# 1   6   7   8   9.0  10.0  11.0
# 2  12  13  14  15.0  16.0  17.0
# 3  18  19  20  21.0  22.0  23.0
# 4  24  25  26  27.0  28.0  29.0
# 5  30  31  32  33.0  34.0  35.0
# 0   0   1   2   NaN   NaN   NaN
# 1   3   4   5   NaN   NaN   NaN
# 2   6   7   8   NaN   NaN   NaN
# 3   9  10  11   NaN   NaN   NaN
# 4  12  13  14   NaN   NaN   NaN

