# Write a program to create a null vector of size 25 but the values from fifth to tenth elements are all 1. by using numpy library.

import numpy as np
x = np.zeros(25) # create a null vector of size 25 and zeros means all values are 0
print("Before: ", x)
x[5:11] = 1
print("After: ", x)
    
