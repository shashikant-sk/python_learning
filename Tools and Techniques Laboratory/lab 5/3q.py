# Write a program to create a vector with 10 random values & sort first half ascending & second half descending by using numpy library.

import numpy as np
x = np.random.random(10)
print("Before: ", x)
x[:10].sort()
x[10:].sort()
x[10:] = x[10:][::-1] # reverse the second half
print("After: ", x)