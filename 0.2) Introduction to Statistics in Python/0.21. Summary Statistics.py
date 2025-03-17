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

