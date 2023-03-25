# A magic square is a square matrix is a matrix all of whose row sums, column sums, and the sums of two diagonals are  the same. (One diagonal of a matrix goes from the top left to the bottom right, the other diagonal goes from top right to om left.) Show by direct computation that if the matrix A is given by 
# A=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
# The matrix A has 5 row sums (one for each row), 5 column sums (one for each column) and two
# diagonal sums. These 12 sums should all be exactly the same, and you could verify that they are the
# same by printing them and “seeing” that they are the same. It is easy to miss small differences among so
# many numbers, though. Instead, verify that A is a magic square by constructing the 5 column sums and
# computing the maximum and minimum values of the column sums. Do the same for the 5 row sums, and compute the two diagonal sums. Check that these six values are the same. If the maximum and
# minimum values are the same, the flyswatter principle says that all values are the same. Hints: The function np.diag extracts the diagonal of a matrix, and the function np.fliplr extracts the other
# diagonal.


import numpy as np

A = np.array([[17, 24, 1, 8, 15],
              [23, 5, 7, 14, 16],
              [4, 6, 13, 20, 22],
              [10, 12, 19, 21, 3],
              [11, 18, 25, 2, 9]])
print(A)

row_sums = A.sum(axis=1) # axis=1 means sum of rows
col_sums = A.sum(axis=0) # axis=0 means sum of columns
diag1_sum = np.diag(A).sum() # diag means diagonal
diag2_sum = np.diag(np.fliplr(A)).sum() # fliplr means flip left to right

sums = np.concatenate((row_sums, col_sums, [diag1_sum], [diag2_sum])) # join two arrays

if np.ptp(sums) == 0: #  peak to peak  difference b/t max and min
  print("A is a magic square.")
else:
    print("A is not a magic square.")
    
    






























# import numpy as np
# A=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
# print("The matrix A is given by: ")
# print(A)
# print("The sum of the rows are: ")
# print(A.sum(axis=1))
# print("The sum of the columns are: ")
# print(A.sum(axis=0))
# print("The sum of the diagonals are: ")
# print(np.diag(A).sum())
# print(np.fliplr(A).diagonal().sum())
# print("The maximum value of the sum of the rows is: ")
# print(A.sum(axis=1).max()) # axis=1 means sum of rows
# print("The minimum value of the sum of the rows is: ")
# print(A.sum(axis=1).min())
# print("The maximum value of the sum of the columns is: ")
# print(A.sum(axis=0).max()) # axis=0 means sum of columns
# print("The minimum value of the sum of the columns is: ")
# print(A.sum(axis=0).min())
# print("The maximum value of the sum of the diagonals is: ")
# print(np.diag(A).sum().max()) 
# print("The minimum value of the sum of the diagonals is: ")
# print(np.diag(A).sum().min())
# print("The maximum value of the sum of the diagonals is: ")
# print(np.fliplr(A).diagonal().sum().max()) # fliplr is use to flip the matrix in left to right direction
# print("The minimum value of the sum of the diagonals is: ")
# print(np.fliplr(A).diagonal().sum().min())

# # Output:
# # The matrix A is given by:
# # [[17 24  1  8 15]
# #  [23  5  7 14 16]
# #  [ 4  6 13 20 22]
# #  [10 12 19 21  3]
# #  [11 18 25  2  9]]
# # The sum of the rows are:
# # [65 75 66 65 65]
# # The sum of the columns are:
# # [65 65 65 65 65]
# # The sum of the diagonals are:
# # 65
