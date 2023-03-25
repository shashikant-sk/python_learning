# Sum all the items in a dictionary python code

# //original
d = {'a': 1, 'b': 2, 'c': 3}
print(sum(d.values()))

# -------------------------------
# modify
def sum_dictionary_items(input_dict):
    if input_dict:
        return sum(input_dict.values())
    return 0

d = {'a': 1, 'b': 2, 'c': 3}
print(sum_dictionary_items(d))
