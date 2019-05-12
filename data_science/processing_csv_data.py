#%%
# # Processing CSV Data

# ## Reading a CSV File

#%%
import os
import pandas as pd
# Returns as a data frame object
pwd = os.getcwd()
csv_file = pwd + "\\data_science\\input.csv"
data = pd.read_csv(csv_file)
print(data)

#%%
# ## Reading specific Rows / Columns

#%%
print("reading first five rows for salary column")
print(data[0:5]['salary'])
print('\n')

print("reading 2 specific columns for all rows")
print(data.loc[:,['salary', 'name']])
