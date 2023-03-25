# 4. Write a program to create a vector of size 10 with values ranging from 0 to 1, both excluded. by uning numpy library.
 
import numpy as np
x = np.linspace(0, 1, 12, endpoint=True)[1:-1] # endpoint=True means include the end points
# linspace is used to create a vector values ( 0 to 1, both excluded)
print(x)