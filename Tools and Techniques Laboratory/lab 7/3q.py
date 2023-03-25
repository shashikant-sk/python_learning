# 3. Write a NumPy program to count the lowest index of "P" in a given array, element-wise.
# Sample Output:
# Original Array:
# ['Python' 'PHP' 'JS' 'EXAMPLES' 'HTML']
# count the lowest index of 'P':
# [ 0 0 -1 4 -1]
 
import numpy as np
arr = np.array(['Python', 'PHP', 'JS', 'java', 'react js'])
print("Original Array: ", arr)
print("count the lowest index of 'P': ", np.char.find(arr, 'P'))
 
    
     
  
  