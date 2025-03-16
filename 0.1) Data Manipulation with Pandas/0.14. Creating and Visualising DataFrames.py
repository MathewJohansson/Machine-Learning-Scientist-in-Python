# This chapter involves:
# - Plotting. 
# - Handling missing data. 
# - Reading data into a DataFrame.

# To display visualisations, matplotlib is needed 
import matplotlib.pyplot as plt

# Histogram showing distribution of a numeric variable 
dog_pack["height_cm"].hist()
plt.show()
#   Select col and add .hist()

# Adjust no. of bins 
dog_pack["height_cm"].hist(bins=5)
plt.show()



# Bar plots 

avg_weight_by_breed = dog_pack.groupby("breed")["weight_kg"].mean()
#   Group by breed as index, weight_kg as first col 

# Then create the bar plot with the mean variable, with a title
avg_weight_by_breed.plot(kind="bar", title="Mean Weight by Dog Breed")
plt.show()



# Line plots

# Sully is a dataset of weight measured each month
sully.head()

# Basic line plot
sully.plot(x="date", y="weight_kg", kind="line")
plt.show()

# Rotates x-axis labels to make them easire to read, especially if they're long
sully.plot(x="date", y="weight_kg", kind="line", rot=45)



# Scatter plots 

dog_pack.plot(x="height_cm", y="weight_kg", kind="scatter")
plt.show()

# Layering plots, alpha makes each transparent so both are always visible 
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist(alpha=0.7)
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7)

# Colour the plots differently 
plt.legend(["F", "M"])
plt.show() 



# E.g., avocados dataset, stating dates of sales, type, year, avg_price, size, and nb_sold

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt 

# Look at the first few rows of the data 
print(avocados.head())

# Total number of avocados sold of each size 
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Bar plot of the number of avocados sold by size, then show the plot 
nb_sold_by_size.plot(kind="bar")
plt.show()


# Total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="nb_sold_by_date", y="date", kind="line")
plt.show()


# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")
plt.show()


# Price of conventional vs. organic avocados 

# Histogram of conventional avg_price, with transparency 0.5, bins = 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins = 20)

# Histogram of organic avg_price, with transparency 0.5 
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins = 20)

# Add a legend and plot 
plt.legend(["conventional", "organic"])
plt.show()



# Missing values - NAN = Not A Number 

# Boolean values for whether values are NA or not 
dogs.isna() 

# True if there are any missing values in that col 
dogs.isna().any()

# Count number of NAN's in that col 
dogs.isna().sum()

# Visualise counts of missing values with a bar plot 
import matplotlib.pyplot as plt 
dogs.isna().sum().plot(kind="bar")
plt.show()

# Remove missing values 
dogs.dropna()

# Replace NAN's with another value, such as 0 
dogs.fillna(0)



# Creating DataFrames 

# A dictionary - each key-value pair is written as "key colon value"
my_dict = {
    "key1": value1, 
    "key2": value2,
    "key3": value3
}

# E.g., 
my_dict = {
    "title": "Charlotte's Web",
    "author": "E.B. White",
    "published": 1952
}

# Access values of a dictionary
my_dict["key1"]


# Two ways to create a DataFrame: from a list of dictionaries, and from a dictionary of lists 
# 1. From a list of dictionaries, it is constructed row by row 
# 2. From a dictionary of lists, it is constructed col by col 


# 1. List of dictionaries:

# Inputting new dog data into a DataFrame. First, create a new list to hold dictionaries 

list_of_dicts = [
    {"name": "Ginger", "breed": "Dachshund", "height_cm": 22, "weight_kg": 10, "date_of_birth": "2019-03-14"},
    {"name": "SCout", "breed": "Dalmation", "height_cm": 59, "weight_kg": 25, "date_of_birth": "2019-05-09"}
]

# Then, convert it into a DataFrame 
new_dogs = pd.DataFrame(list_of_dicts)


# 2. Dictionary of lists: 

# First create a dictionary 
dict_of_lists = {
    "name": ["Ginger", "Scout"],
    "breed": ["Dachshund", "Dalmation"],
    "height_cm": [22, 59],
    "weight_kg": [10, 25],
    "date_of_birth": ["2019-03-14", "2019-05-09"]
}

# Then convert it into a DataFrame 

new_dogs = pd.DataFrame(dict_of_lists)



# Reading and writing CSVs 

# new_dogs.csv has the CSV file contents: 
# name,breed,height_cm,weight_kg,d_o_b
# Ginger,Dachshund,22,10,2019-03-14
# Scout,Dalmation,59,25,2019-05-09

# Put this CSV into a DataFrame 
import pandas as pd 
new_dogs = pd.read_csv("new_dogs.csv")
print(new_dogs)

# Add a bmi index column to new_dogs 
new_dogs["bmi"] = new_dogs["weight_kg"] / (new_dogs["height_cm"] / 100) ** 2

# Create an updated CSV file 
new_dogs.to_csv("new_dogs_with_bmi.csv")
#   this will then have the original CSV file contents with a bmi col added on 

