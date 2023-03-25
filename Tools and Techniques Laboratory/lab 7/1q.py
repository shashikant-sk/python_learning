# 1. Write a NumPy program to concatenate element-wise two arrays of string.

# Sample Output:
# Array1:
# ['Python' 'PHP' ]
# Array2:
# [' Java' ' C++']
# new array:
# ['Python Java' 'PHP C++']



import numpy as np

n = int(input("Enter the number of elements in the array: "))
print("Enter the elements of the array: ")
arr1 = np.array([input() for i in range(n)])
print("Enter the elements of the array: " )
arr2 = np.array([input() for i in range(n)])
print("New array: {", end = " ")
# add space between the elements of the array
new_arr = []
for i in range(n):
   new_arr.append(arr1[i] + " " + arr2[i])
print(" ".join(new_arr), end = " ")
#

 
 