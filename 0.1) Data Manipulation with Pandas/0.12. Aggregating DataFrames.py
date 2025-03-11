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

