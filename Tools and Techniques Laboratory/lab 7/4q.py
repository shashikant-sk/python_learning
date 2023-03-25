# 4. Write a NumPy program to count a given word in each row of a given array of string values. Sample output:
# Original array of string values:
# [['Python' 'NumPy' 'Exercises']
# ['Python' 'Pandas' 'Exercises']
# ['Python' 'Machine learning' 'Python']]
# Count 'Python' row wise in the above array of string values:
# [[1 0 0]
# [1 0 0]
# [1 0 1]]

import numpy as np
arr = np.array([['Python ', 'NumPy', 'Exercises'], ['Python', 'Pandas', 'Exercises'], ['Python', 'Machine learning', 'Python']])
print("Original array of string values : ", arr)
print("Count 'Python' row wise in the above array of string values : ", np.char.count(arr, 'Python'))
    
    