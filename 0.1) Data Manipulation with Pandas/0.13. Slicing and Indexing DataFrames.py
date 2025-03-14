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



# Slicing lists - selecting consecutive elements from objects. 

# E.g., 
breeds = ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"]
breeds[2:5] # prints out the 3rd, 4th, and 5th elements in the list (5 not included). 

# For all
breeds[:]

# Sort the index before slicing 
dogs_srt = dogs.sort_index(["breed", "color"]).sort_index()

# Slice rows at the outer level of an index
dogs_srt.loc["Chow Chow":"Poodle"]
# index values rather than numbers are stated to access indexes

# Slicing inner index levels correctly - pass the first and last positions 
#                                        as tuples
dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey")]


# Slicing columns 
dogs_srt.loc[:, "name":"height_cm"]

# Slicing cols and rows at the same time 
dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey"), "name":"height_cm"]


# Subset DataFrames by a range of dates 
dogs = dogs.set_index("date-of-birth").sort_index()

# Slicing by dates 
dogs.loc["2014-08-25":"2016-09-16"]

# Slicing between 2014-01-01 and 2016-12-31
dogs.loc["2014":"2016"]


# Slicing using iloc method
dog.iloc[2:5, 1:4]

# -----------------------------

# E.g., temperatures of cities
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])


# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])


# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08-01":"2011-02-28"])



# Working with pivot tables 

