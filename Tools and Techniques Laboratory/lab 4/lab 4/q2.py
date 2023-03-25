def multiplyList(myList):

	result = 1
	for x in myList:
		result = result * x
	return result

list1 = [9, 2, 3, 4]
list2 = [11, 22, 33]
print(multiplyList(list1))
print(multiplyList(list2))
