# Field of statistics - the practice and study of collecting and 
#                       analysing data. 

# A summary statistic - a fact about or summary of some data. 


# Types of statistics:
# 1. Descriptive statistics - describe and summarise data. 
#    E.g., 50% of friends drive to work. 
#          25% take the bus. 

# 2. Inferential statistics - use a sample of data to make inferences
#                             about a larger population. 
#    E.g., what percentage of people drive to work, based on our data?


# Types of data:
# 1. Numeric (quantitative):
#    - Continuous (measured). E.g., speed or time. 
#    - Discrete (counted). E.g., no. of pets or packages. 

# 2. Categorical (qualitative). 
#    - Nominal (unordered). E.g., married/unmarried, country of residence. 
#    - Ordinal (ordered). E.g., survey answers (str. disagree - neither - str. agree, etc.)

#   Categorical data can be represented as numbers. E.g.: 
#   - Nominal - married/unmarried (1/0)
#   - Ordinal - str. disagree (1) - neither (3) - str. agree (5)


# For numerical data, summary statistics and plots such as scatterplots are ideal. 
# For categorical data, counts and barplots are ideal. 


# Three measures of center: mean, median, mode. 

# Mean = the average; add all numbers and divide by total number of data points. 
import numpy as np
np.mean()

# Median = sort all data points and take the middle one. 
msleep['sleep_total'].sort_values() # or:
np.median(msleep['sleep_total']) 

# Mode = most frequency value 
msleep['sleep_total'].value_counts() # or:
import statistics 
statistics.mode(msleep['vore'])

# Adding an outlier 
# Subset msleep to select rows where 'vore' equals 'insecti' 
msleep[msleep['vore'] == 'insecti']
#   essentially all insectivores in the dataset. 

# Mean and median of insectivore sleep times 
msleep[msleep['vore'] == 'insecti']['sleep_total'].agg([np.mean, np.median])

# Now an insect has been added that never sleeps - the above code will produce very 
#                                                  different results
# The mean will go down significantly, but not so much the median. 
# The mean is more sensitive to extreme values than the median. 

# As the mean is more sensitive to extreme values, it's better for symmetrical data. 

# Skew: 
# Left-skewed data means the peak is to the right, with a tail trailing down toward the left. 
# Right-skewed data is the opposite. 

# The mean is pulled in the direction of the skew. 



# E.g.: food_consumption dataset of countries, on kg of food per person per year in each country.
#       incl. food category (consumption) and carbon footprint (co2_emissions). 

import numpy as np 
# Subset country for USA 
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Mean and median consumption for USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# Import matplotlib.pylot, subset for rice food_category, then plot .hist() for rice and show
import matplotlib.pyplot as plt 
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
rice_consumption['co2_emission'].hist()
plt.show()



# Measures of spread - how spread apart or close together data points are.

# 1st measure = variance; average distance from each data point to the data's mean
# To calculate, calculate distance between each point and the mean = one number for every data point.
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])

# then square each distance, and add them all together 
sq_dists = dists ** 2
sum_sq_dists = np.sum(sq_dists) 

# finally, divide by number of data points -1 
variance = sum_sq_dists / (83 - 1)

# the variance here is squared, so np.var is used
np.var(msleep['sleep_total'], ddof=1)
# ddof=1 is for sample variance. Remove this for population variance. 


# 2nd measure = standard deviation; square root of the variance 

# Two ways of writing this
np.sqrt(np.var(msleep['sleep_total'], ddof=1))
np.std(msleep['sleep_total'], ddof=1)


# 3rd measure = mean absolute deviation; this takes the absolute values of the distances
#               to the mean, then takes the mean of those differences. 

dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])
np.mean(np.abs(dists))

