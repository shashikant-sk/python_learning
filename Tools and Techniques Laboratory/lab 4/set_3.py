# Remove items from Python set

# original
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("\nAfter removing the first element from the said set:")
print(num_set)

# ----------------------------------------
 
#  modified
def remove_all_elements(num_set):
    while num_set:
        num_set.pop()
    return num_set
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
print("\nAfter removing all elements from the said set:")
print(remove_all_elements(num_set))
