# Assuming normality, construct the confidence interval
from scipy.stats import t
import numpy as np
from math import sqrt
import scipy.stats as stats

# Create a random vector of 30 numbers from the normal distribution

Data_vec = stats.norm.rvs(size = 30)

# Compute the mean of this vector

Mean_for_data =  np.average(Data_vec)

# Compute the standard deviation (or variance and take the sqrt of that)

SDev_for_data = np.std(Data_vec, ddof=1)

# Compute the classical confidence interval
Confidence_for_data = [Mean_for_data + val * SDev_for_data / sqrt(len(Data_vec)) for val in t.interval(0.95, len(Data_vec) - 1)]
<<<<<<< HEAD
<<<<<<< HEAD
print(Confidence_for_data )
=======

>>>>>>> 036367a6aad4a887a3d52b3cad2d170153f71140
=======
print(Confidence_for_data )
>>>>>>> d46954cd5e7783041a111cdd734fec00ff86db88
# Compute with Bayes
stats.bayes_mvs(Data_vec, alpha=0.95)