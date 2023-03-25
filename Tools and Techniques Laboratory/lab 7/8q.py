# 8. WAP to generate a 1-D array of 10 random integers. Each integer should be a number between 30
# and 40 (inclusive)
# Sample output:

# [36, 30, 36, 38, 31, 35, 36, 30, 32, 34]
  
import numpy as np
arr = np.random.randint(30, 41, 10)
print(arr)
 
  