# 5. Write a program to concatenate element-wise two arrays of string by using numpy library.
 
import numpy as np
x = np.array(['a', 'b', 'c'])
y = np.array(['d', 'e', 'f'])
print(np.char.add(x, y)) 
    