# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
  
import pandas as pd
import numpy as np
d1 = pd.Series([2, 4, 6, 8, 10])
d2 = pd.Series([1, 3, 5, 7, 9])
print("Original Series:")
print(d1.tolist() )
print(d2.tolist() )
print("Add two Series:", (d1 + d2).tolist() )
print("Subtract two Series:", (d1 - d2).tolist() )
print("Multiply two Series:", (d1 * d2).tolist() )
print("Divide Series1 by Series2:", (d1 / d2).tolist() )

    

 