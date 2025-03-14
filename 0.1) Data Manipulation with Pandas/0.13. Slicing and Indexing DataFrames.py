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

# Using the dataset dog_pack, remember that this is how to create a pivot table
dogs_height_by_breed_vs_color = dog_pack.pivot_table(
    "height_cm", index="breed", columns="color")
#   First argument = column name, index argument lists cols to group by, and the 
#                       columns argument lists the cols to group by and display in cols

# Pivot tables are just DataFrames with sorted indexes. 

# loc and slicing combo is ideal for subsetting pivot tables: 
dogs_height_by_breed_vs_color.loc["Chow Chow":"Poodle"]

# Calculating summary statistics, e.g., for mean.
# It uses axis argument whereby default value is "index". 
# This just means to calculate the given statistic across rows. 
dogs_height_by_breed_vs_color.mean(axis="index")
# This will produce: an index for the colours of dogs, and the first col is mean of colours
# The behaviour is the same if we don't specify axis="index"

# Calculating summary stat across the cols
dogs_height_by_breed_vs_color.mean(axis="columns")
# The mean height is calculated for each breed

# The above calculations are only possible in pivot tables where data types are the same



# Add a year column to temperatures (accesses components of a date)
temperatures["year"] = temperatures["date"].dt.year

# Worldwide mean temperature by year 
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temperature
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Mean temp by city 
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temperature
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])

