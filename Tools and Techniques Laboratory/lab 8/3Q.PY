# Write a Pandas program to convert a NumPy array to a Pandas series.

import pandas as pd
import numpy as np
d1 = np.array([10, 20, 30, 40, 50])
print("Original array:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)
    
        