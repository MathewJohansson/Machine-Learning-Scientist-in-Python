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

# Sort first by weight, then by height (put both sets into lists = [] )
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

# To do the above subsetting of multiple conditions on one line
dogs[ (dogs["breed"] == "Labrador") & (dogs["color"] == "Brown") ]

# Filter for multiple values of a categorical variable (e.g., color type)
is_black_or_brown = dogs["color"].isin(["Black", "Brown"]) 
dogs[is_black_or_brown]

# Another example of the above 
# The Mojave Desert states 
canu = ["California", "Arizona", "Nevada", "Utah"]
# Filter for rows in the Mojave Desert states 
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]
print(mojave_homelessness)



# New Columns

dogs["height_m"] = dogs["height_cm"] / 100
# creates a new col called height_m which is the height in metres

dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"] ** 2
# creates a new col called bmi

# Multiple manipulations, finding all skinny dogs

bmi_lt_100 = dogs[dogs["bmi"] < 100] # bmi > 100
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending=False) # Sort in desc. order,
                                                                      # tallest skinny dogs at top.
bmi_lt_100_height[["name", "height_cm", "bmi"]] # Produce only the 3 cols we're interested in.

