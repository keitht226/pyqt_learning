#%% [markdown]

# # Python - Data Operations
#
# ## Working with np.array

#%%
import numpy as np

# more than one dimension
a = np.array([[1, 2], [3, 4]])
print(a)

#%%
import numpy as np
# set minimum dimensions
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)

#%%
import numpy as np
# Set the datatype
a = np.array([1, 2, 3], dtype=complex)
print(a)

#%% [markdown]

# ## Working with pandas

#%%
import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
# Series contains any data type (heterogenous) and is constructed with:
#   pandas.Series(data, index, dtype, copy)
s = pd.Series(data)
print(s)

#%%
import pandas as pd

data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
# data frame is 2 dimensions and data is aligned ina tabular fashion
#   pandas.DataFrame(data, index, columns, dtype, copy)
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)
