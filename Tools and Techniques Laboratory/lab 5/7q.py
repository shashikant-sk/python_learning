# 7. Write a program to create a 2D array with 1 on the border and 0 inside by using numpy library. 

import numpy as np
x = np.ones((5, 5)) # 5x5 matrix  np.ones 
print("Before: ", x)
x[1:-1, 1:-1] = 0   # 1:-1 means from 1 to last-1
print("After: ", x)

    
 