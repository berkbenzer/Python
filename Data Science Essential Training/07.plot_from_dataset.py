import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

data_filename = 'Advertising.csv'

df = pd.read_csv(data_filename)

df_new = df.head(7)
data = np.array(df_new)
indices = np.argsort(data[:,0])
sorted_data = data[indices]
sorted_tv_column = sorted_data[:, 0]
sorted_sales_column = sorted_data[:, 3]

plt.scatter
plt.plot(sorted_tv_column, sorted_sales_column)
plt.xlabel("Tv budget")
plt.ylabel("Sales")

plt.title("Budget-Sales")
plt.show()
