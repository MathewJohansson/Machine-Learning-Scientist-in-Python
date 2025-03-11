# This chapter involves:
# - Summary statistics. 
# - Counting. 
# - Grouped summary statistics.



# Summary Statistics

#  Mean of a col
dogs["height_cm"].mean()

# Other summary functions include:
# .median()
# .mode()
# .min()
# .max()
# .var()
# .std()
# .sum()
# .quantile()

# E.g., oldest and youngest dog
dogs["date-of-birth"].min()
dogs["date-of-birth"].max()



# Compute custom summary statistics
def pct30(column):
    return column.quantile(0.3)
    # creates function pct30 that computes 30th percentile of a DataFrame col.

dogs["weight_kg"].agg(pct30)
    # .agg allows us to use the new function pct30 on weight_kg
    # Finds 30th percentile of weight_kg

# On two columns at the same time
dogs[["weight_kg", "height_cm"]].agg(pct30)

# Second function for 40th percentile, then use both on weight_kg
def pct40(column):
    return column.quantile(0.4)
dogs["weight_kg"].agg([pct30, pct40])



# Cumulative total - adding each row value to the sum
dogs["weight_kg"].cumsum()

# Other cumulative statistics:
# .cummax()
# .cummin()
# .cumprod()


# E.g., cumulative statistics for store department sales:

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1.weekly_sales.cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1.weekly_sales.cummax()

print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])



# Counting

# vet_visits = df on dog visits to a vet

# Drop duplicate names - but two dogs may have the same name
vet_visits.drop_duplicates(subset="name")

# Drop duplicates where name and breed are the same
unique_dogs = vet_visits.drop_duplicates(subset=["name", "breed"])
print(unique_dogs)

# Counts dogs of each breed 
unique_dogs["breed"].value_counts()

# Order them in breed counts, highest number first
unique_dogs["breed"].value_counts(sort=True) 

# State proportions of each breed out of total 
unique_dogs["breed"].value_counts(normalize=True)



# -------------------------------

# E.g., sum of sales, weekly sales for each store, proportions for each store, and group by.

sales_all = sales["weekly_sales"].sum()

# Subset for type A, B, and C stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# -------------------------------


# Grouped summary statistics

# Group by colour of dog, select weight col, and take the mean 
dogs.groupby("color")["weight_kg"].mean()

# Multiple grouped summaries (for minimum, maximum, and sum of the groups)
dogs.groupby("color")["weight_kg"].agg([min, max, sum])
#                                  Remember to use the .agg() function. 

# Group by mutiple variables (colour and breed)
dogs.groupby(["color", "breed"])["weight_kg"].mean()

# Many groups, many summaries 
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()



# Pivot tables

# Instead of grouping by colour, and calculating mean weights like before:
dogs.groupby("color")["weight_kg"].mean()
#   we can do the same thing using the pivot_table method:
dogs.pivot_table(values="weight_kg", index="color")
#       pivot_table takes the mean by default.


# Using a different summary statistic 
import numpy as np 
dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median)

# Multiple summary statistics 
dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.mean, np.median])


# Instead of computing mean weight by two variables like before:
dogs.groupby(["color", "breed"])["weight_kg"].mean()
#   we can do the same thing using the pivot_table method:
dogs.pivot_table(values="weight_kg", index="color", columns="breed")
#   - This creates a table, whereby NAs exist where there are no breeds of certain colours.

# Change the above outcome table to display 0s instead of NAs
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0)

# margins=True sets last col to be the mean of all rows 
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0, margins=True)

