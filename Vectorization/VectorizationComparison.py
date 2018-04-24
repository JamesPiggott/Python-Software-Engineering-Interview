'''
Created on April 24 2018

@author: James Piggott

Basic speed test between Vectorized operations and For-loop operations
'''

import numpy as np
import time

# We begin this test by just creating a simple 4 value vector with numpy. We print it to check we get what we want
a = np.array([1,2,3,4])
print("A simple vector: ", a)

# Create two vectors a and b, each holding 10 million randomly generated numbers
a = np.random.rand(10000000)
b = np.random.rand(10000000)

# Next we calculate the time it is need to erform a vectorized calculation with numpy
start = time.time()

# Then we perform the matrix multiplication with the np.dot() function
c = np.dot(a, b)

end = time.time()

# By subtracting the time the operation ended with the start we get the time needed
print("Vectorized version: " + str(1000 * (end - start)) + "ms")

# In the second test we just use a for loop to perform the calculations
c = 0
start = time.time()

for i in range(10000000):
    c = a[i]+b[i]

end = time.time()

print("For loop: " + str(1000 * (end - start)) + "ms")
print("The speed difference should be a factor 300. Now you know why GPUs are popular to use for vector operations")
