# This chapter involves:
# - Subsetting and slicing. 
# - Indexes and subsetting using indexes. 



# Explicit Indexes

# Setting a column as the index
dogs_ind = dogs.set_index("name")
print(dogs_ind)

# To undo 
dogs_ind.reset_index()

# Remove/drop an index
dogs_ind.reset_index(drop=True)

# Indexes make subsetting simpler. Instead of: 
dogs[dogs["name"].isin(["Bella", "Stella"])]
# we can use: 
dogs_ind.loc[["Bella", "Stella"]]


# Index values don't need to be unique
dogs_ind2 = dogs.set_index("breed")

# then subset on Labrador for those rows
dogs_ind2.loc["Labrador"]


# Multi-level indexes (hierarchical indexes)
dogs_ind3 = dogs.set_index(["breed", "color"])
# this puts breed as the left-most index col, and color to the right of that.

# Subset the outer level with a list 
dogs_ind3.loc[["Labrador", "Chihuahua"]]

# Subsetting on inner levels 
dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]]


# Sort by index values
dogs_ind3.sort_index()

# Controlling sort_index, sorts each index value
dogs_ind3.sort_index(level=["color", "breed"], ascending=[True, False])


# Problems with indexes:
# - Index values are just data. 
# - Indexes violate "tidy data" principles. 
# - Two syntaxes need to be learned. 

