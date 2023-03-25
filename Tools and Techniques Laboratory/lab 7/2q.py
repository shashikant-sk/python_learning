# 2. Write a NumPy program to split the element of a given array with spaces. 

# Sample Output:
# Original Array:
# ['Python PHP Java C++']
# Split the element of the said array with spaces:
# [list(['Python', 'PHP', 'Java', 'C++'])]

import numpy as np
  
arr = np.array(['Python PHP julia helloworld'])
print("Original Array: ", arr)
print("Split the element of the said array with spaces: ", np.char.split(arr))
     
     
     
    #  import numpy as np
    #  newArray = np.array(input('Enter the elements of the array: ').split())
    #  print("New array: {", end = " ")
    


