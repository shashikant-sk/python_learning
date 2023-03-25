# 7. WAP to Convert a 1-D array into a 2-D array with 3 rows
# Sample output:
# Start with: exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
# Desired output:
# [[ 0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]]

import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print("Start with: ", arr)
print("Desired output: ")
print(arr.reshape(3, 3))
   