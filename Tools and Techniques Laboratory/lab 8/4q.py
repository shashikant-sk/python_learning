# Write a Pandas program to convert a given Series to an array.

import pandas as pd
import numpy as np
d1 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print(d1.tolist() )
print("Series to an array:")
print(d1.values)

        