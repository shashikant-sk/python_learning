# 6. write a program to create a 4X3 array with random values & find out the minimum & maximum values by using numbpy library.

import numpy as np
x = np.random.random((4, 3)) 
print("Array: ", x)
print("Minimum: ", x.min())
print("Maximum: ", x.max())
