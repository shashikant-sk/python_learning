# Write a Python program to add an item to a tuple

# original
t = (1, 2, 3)
# convert tuple to list
lst = list(t)
# add item to list
lst.append(4)
# convert list back to tuple
new_tuple = tuple(lst)
print(new_tuple) # (1, 2, 3, 4)
# ---------------------

# modified
def add_item_to_tuple(t, item):
    # convert tuple to list
    lst = list(t)

    # add item to list
    lst.append(item)

    # convert list back to tuple
    new_tuple = tuple(lst)

    # return the new tuple
    return new_tuple

# original tuple
t = (1, 2, 3)

# add item to tuple
new_tuple = add_item_to_tuple(t, 4)

# result
print(new_tuple) # (1, 2, 3, 4)
