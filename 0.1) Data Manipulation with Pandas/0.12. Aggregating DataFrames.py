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

