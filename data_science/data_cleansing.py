#%% [markdown]
# # Data cleansing
# ## Example of missing data

#%%
import pandas as pd
import numpy as np

# Creates a matrix of random float values following a gaussian distribution
df = pd.DataFrame(np.random.randn(5, 3),
                  index=['a', 'd', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three'])

# Add more indecies than there were originally to represent missing data
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("Original Matrix with missing data: ")
print(df)
print('\n')

#%% [markdown]
# ## Find the missing data

#%%
# Detect if a location is missing with df.isnull() and df.notnull()
# or pd.isnan() for individual values
print("Check for null values in single column: ")
print(df['one'].isnull())
print('\n')

print("Check if specific element is null: ")
print(pd.isnull(df['one']['b']))

#%%
## Replace the missing data

#%%
# Replace missing data with a scalar using df.fillna
#   df.fillna(self, value=None, method=None, axis=None, inplace=False,
#             limit=None, downcast=None, **kwargs)
# Note that assigning a new df object from an existing one is
# typically done by reference and if inplace=True the original object
# will modified
#
# method options: backfill/bfill, pad/ffill, None
tmp = df
# creates a true copy at this point
tmp = tmp.fillna(0)
print("Replace missing data with scalar: ")
print(tmp)
print('\n')

# Pad values with previous non NaN row
tmp = df
tmp = tmp.fillna(method='pad')
print("Replace missing data with padding: ")
print(tmp)
print('\n')

# Pad values with following non NaN row
tmp = df
tmp = tmp.fillna(method='bfill')
print("Replace missing data with padding: ")
print(tmp)

#%%
# ## Remove the missing data

#%%
# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#   axis: 0/'index', 1/'columns'
#   how: 'any', 'all': drop row/col if at least one or all values
#        are Nan respectively
tmp = df
tmp = tmp.dropna()
print(tmp)

#%%
## Replace non-NaN values

#%%
# Similar to fillna, non-Nan values can be replaced
# df.replace(to_replace=None, value=None, inplace=False,
#            limit=None, regex=False, method='pad')
df = pd.DataFrame({
    'one': [10, 20, 30, 40, 50, 2000],
    'two': [1000, 0, 30, 40, 50, 60]
})
print(df.replace({1000: 10, 2000: 60}))
