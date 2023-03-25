# write a program to create a vector with values ranging from 5 to 20 reverse it by using numpy library.

import numpy as np
x = np.arange(5, 21)  # arange means range of values
print("Before: ", x)
x = x[::-1]
print("After: ", x)
    