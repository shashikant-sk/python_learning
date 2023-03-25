# Write a Pandas program to convert Series of lists to one Series.
 
import pandas as pd
import numpy as np 
d1 = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
print("Original Series:")
print(d1.tolist() )
print("One Series:")
print(d1.apply(pd.Series).stack().reset_index(drop=True))


