# Write a Pandas program to get the first 3 rows of a given DataFrame.

import pandas as pd
df = pd.DataFrame({'col1': [1, 2, 3, 4, 7, 11],
                    'col2': [4, 5, 6, 9, 10, 8], 
                    'col3': [7, 8, 12, 11, 17, 27],
                    'col4': [7, 8, 12, 11, 17, 27],
                    'col5': [7, 8, 12, 11, 17, 27],
                    'col6': [7, 8, 12, 11, 17, 27],
                    'col7': [7, 8, 12, 11, 17, 27],
                    'col8': [7, 8, 12, 11, 17, 27],
                    'col9': [7, 8, 12, 11, 17, 27],
                    'col10': [7, 8, 12, 11, 17, 27],})
print("Original DataFrame:")
print(df)
print("First three rows of the data frame:")
print(df.iloc[:3])
 
 