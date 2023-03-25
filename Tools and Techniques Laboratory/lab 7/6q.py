# 6. WAP to delete the second column from a given array and insert the following new column in its
# place.

# Sample output:
# Printing Original array
# [[34 43 73]
# [82 22 12]
# [53 94 66]]

# Array after deleting column 2 on axis 1
# [[34 73]
# [82 12]
# [53 66]]

# Array after inserting column 2 on axis 1
# [[34 10 73]
# [82 10 12]
# [53 10 66]]

import numpy as np
arr = np.array([[44, 53, 83], [72, 33, 23], [43, 54, 44]])
print("Printing Original array")
print(arr)
print("Array after deleting column 2 on axis 1")
arr = np.delete(arr, 1, axis = 1)
print(arr)
print("Array after inserting column 2 on axis 1")
arr = np.insert(arr, 1, 10, axis = 1)
print(arr)
    