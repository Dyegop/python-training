import scipy.linalg as la
import scipy.stats as st
import numpy as np


# Exercise 1:
# There is a test with 30 questions worth 150 marks. The test has two types of questions:
# 1. True or false – carries 4 marks each
# 2. Multiple-choice – carries 9 marks each
# Find the number of true or false and multiple-choice questions.

# Formulate two linear equations based on the given scenario
# 4x + 9y = 150
# x + y = 30

# Apply a suitable method to solve the linear equation
matrix = np.array(([4, 9], [1, 1]))
matrix2 = np.array([150, 30])
print(la.solve(matrix, matrix2))





# Exercise 1:
# Use SciPy to declare 20 random values for random values and perform
# 1. CDF – Cumulative Distribution Function for a random variable 10, with loc 1 and scale 3
# 2. PDF – Probability Density Function for a random variable 14, wit loc 1 and scale 1

# Define 20 random variables
values = st.norm.rvs(loc=0, scale=1, size=20)

# Perform Cumulative Distribution Function or CDF on variables, with loc 1 and scale 3
result_cdf = st.norm.cdf(10, loc=1, scale=3)

# Perform Probability Density Function or PDF on variables, with loc 1 and scale 1
result_pdf = st.norm.pdf(14, loc=1, scale=1)

print(values)
print(result_cdf)
print(result_pdf)
