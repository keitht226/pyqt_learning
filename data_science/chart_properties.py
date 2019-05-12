#%% [markdown]
# # Chart Properties

## Creating a chart

#%%
import numpy as np
import matplotlib.pyplot as plt

# Returns evenly spaced values withing provided range
# exclusive of endpoint.
x = np.arange(0,10)
y = x ^ 2

# Label title and axes
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")

# Format the line colors and type (see options below)
plt.plot(x,y,'m')
plt.plot(x,y,'w+')

plt.plot(x,y)
# Save as pdf
# plt.savefig('filename.pdf', format='pdf')

#%% [markdown]
# ## Formatting options
# | **Symbol** | **Effect** |
# | :--------- | :--------- |
# | 'b'	       | blue       |
# | 'g'	       | green      |
# | 'r'	       | red        |
# | 'c'	       | cyan       |
# | 'm'	       | magenta    |
# | 'y'	       | yellow     |
# | 'k'	       | black      |
# | 'w'	       | white      |
#   
# | **Symbol** | **Effect**             |
# | :--------- | :--------------------- |
# | '.'	       | point marker           |
# | ','	       | pixel marker           |
# | 'o'	       | circle marker          |
# | 'v'	       | triangle_down marker   |
# | '^'	       | triangle_up marker     |
# | '<'	       | triangle_left marker   |
# | '>'	       | triangle_right marker  |
# | '1'	       | tri_down marker        |
# | '2'	       | tri_up marker          |
# | '3'	       | tri_left marker        |
# | '4'	       | tri_right marker       |
# | 's'	       | square marker          |
# | 'p'	       | pentagon marker        |
# | '*'	       | star marker            |
# | 'h'	       | hexagon1 marker        |
# | 'H'	       | hexagon2 marker        |
# | '+'	       | plus marker            |
# | 'x'	       | x marker               |
# | 'D'	       | diamond marker         |
# | 'd'	       | thin_diamond marker    |
# | '|'	       | vline marker           |
# | '_'	       | hline marker           |
#   
# | **Symbol** | **Effect**          |
# | :--------- | :-------------------|
# | '-'	       | solid line style    |
# | '--'       | dashed line style   |
# | '-.'       | dash-dot line style |
# | ':'	       | dotted line style   |