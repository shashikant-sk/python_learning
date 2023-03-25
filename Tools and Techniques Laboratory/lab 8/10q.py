import pandas as pd
import numpy as np
exam_data  = {'name': ['Anas', 'Mia', 'Kath', 'John', 'Rishab', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'gender': ['M', 'F', "F", 'M', 'M', 'F', 'M', 'F', 'F', 'M'],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("Original rows:")
print(df)
print("\nAppend a new row:")
df.loc['k'] = ['Aman', 'F', 2, 'yes']
print("Print all records after insert a new record:")
print(df)
print("\nDelete the new row and display the original  rows:")
df = df.drop('k')
print(df)
