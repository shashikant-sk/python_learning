# Python program to interchange first and last elements in a list

    
    # Original
    
# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

# ----------------------

# modified
def swap_first_last(input_list):
    if input_list:
        first = input_list[0]
        last = input_list[-1]
        input_list[0] = last
        input_list[-1] = first
        return input_list
    return []

input_list = [1, 2, 3, 4, 5]
print(swap_first_last(input_list))
