def swapList(newList):
	size = len(newList)
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
newList = [12,35,26,17,28]
print("Original list-->",newList)
print(swapList(newList))
