# Merge two Python dictionaries 

#  original
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)

# -----------------------
#  modfiied
# If you want to keep the original dictionaries unchanged and create a new dictionary with the merged key-value pairs, you can use the {**dict1, **dict2}
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)
