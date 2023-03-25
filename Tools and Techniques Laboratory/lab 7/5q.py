# 5. WAP to print max from axis 0 and min from axis 1 from the following 2-D array.
# Sample output:
# Printing Original array
# [[34 43 73]
# [82 22 12]
# [53 94 66]]

# Printing amin Of Axis 1
# [34 12 53]

# Printing amax Of Axis 0
# [82 94 73]

import numpy as np
arr = np.array([[24, 43, 93], [52, 33, 11], [33, 34, 55]])
print("Printing Original array")
print(arr)
print("Printing amin Of Axis 1")
print(np.amin(arr, axis = 1)) # axis = 1 means row wise operation and amin use to find minimum value
print("Printing amax Of Axis 0") # axis = 0 means column wise operation and amax use to find maximum value
print(np.amax(arr, axis = 0))

        
