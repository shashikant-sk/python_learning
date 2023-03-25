# 9. WAP to Replace all odd numbers in the given array with -1
# Sample output:
# Start with: exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Desired output:
# [ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1]


import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Start with: ", arr)
print("Desired output: ")
arr[arr % 2 == 1] = -1
print(arr)
    