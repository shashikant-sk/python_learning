# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.

import pandas as pd
import numpy as np

exam_data  = {'name': ['Anas', 'Mia', 'Kath', 'John', 'Rishab', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'gender': ['M', 'F', "F", 'M', 'M', 'F', 'M', 'F', 'F', 'M'],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Initial data: \n")
print(df)
print("\n\n**********Selected specific columnsdisplayed:**********\n")
print(df[['name', 'gender']])
