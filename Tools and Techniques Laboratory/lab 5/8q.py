# 8. Write a program to create a 4 X 4 matrix with values 1,2,3,4 just below & above the diagonal , rest zeros by using numpy library.

import numpy as np  
x = np.diag(1+np.arange(4), k=-1) # k=-1 means below the diagonal and diag means diagonal
print(x)
    
    