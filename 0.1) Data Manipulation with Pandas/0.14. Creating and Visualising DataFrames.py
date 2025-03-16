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

