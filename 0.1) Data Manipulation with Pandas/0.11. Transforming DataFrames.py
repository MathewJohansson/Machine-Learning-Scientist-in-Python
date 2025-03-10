# This chapter involves:
# - Sorting and subsetting. 
# - Creating new columns. 

# Pandas is built on top of: 
# 1. NumPy - provides multi-dimensional array objects for easy data 
# #   manipulation that Pandas uses to store data. 
# 2. Matplotlib - provides powerful data visualisation capabilities that
#     Pandas takes advantage of. 

# Rectangular data/tabluar data is the most common form of data storage. 
# Rectangular data = DataFrame. 

# Different cols can contain different data types. 
# Same col only contains same data type.

print(dataframename.head()) # Shows the first 5 rows of the DataFrame.

print(dataframename.info()) # Shows the data types of each col and the 
#                               number of non-missing values.

print(dataframename.shape) # Shows the number of rows and cols in the 
#                                DataFrame.

print(dataframename.describe()) # Shows the summary statistics of the
#                                   DataFrame.

print(dataframename.values) # Shows the values of the DataFrame as a
#                                 2D NumPy array.  

print(dataframename.columns) # Shows the column names of the DataFrame.

print(dataframename.index) # Shows the index of the DataFrame.


# Pandas Philosopy:
#   There should be one - and preferably only one - obvious way to do it.


