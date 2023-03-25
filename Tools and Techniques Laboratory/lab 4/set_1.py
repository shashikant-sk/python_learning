# Python | Maximum and Minimum in a Set

# // Original

def MAX(sets):
	return (max(sets))
	
# Driver Code
sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(MAX(sets))
#  ----------------------------------

# modifed

def get_max_element(input_set):
    if input_set:
        return max(input_set)
    return None

input_set = {8, 16, 24, 1, 25, 3, 10, 65, 55}
print(get_max_element(input_set))
