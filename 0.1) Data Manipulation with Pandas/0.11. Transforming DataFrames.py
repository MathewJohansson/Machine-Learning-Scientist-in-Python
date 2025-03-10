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



# Basic commands

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



# Sorting

dogs.sort_values("weight_kg") # Sorts the DataFrame by the values of the
#                                 specified col, weight_kg

dogs.sort_values("weight_kg", ascending=False) # Sorts the DataFrame by the 
#                                                  values of the specified col,
#                                                  weight_kg, in descending order.

# Sort first by weight, then by height
dogs.sort_values(["weight_kg", "height_cm"], ascending=[True, False])

# Select just one col 
dogs["name"]

# Select multiple cols
dogs["breed", "height_cm"]

# Alternative way 
cols_to_subset = ["breed", "height_cm"]
dogs[cols_to_subset]

# Subsetting rows (filter against)
dogs["height_cm"] > 50 # produces boolean results for heights > 50

# Subsetting for the rows > 50, produces all cols for each row
dogs[dogs["height_cm"] > 50]

# Subset based on text data (by breed)
dogs[dogs["breed"] == "Labrador"] 

# Subset based on dates (dogs born before 1st Jan 2015)
dogs[dogs["date_of_birth"] < "2015-01-01"]

# Subset multiple conditions
is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "Brown"
dogs[is_lab & is_brown]

