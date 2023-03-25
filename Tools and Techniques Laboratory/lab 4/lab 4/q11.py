
def Merge(dict1, dict2):
	return(dict2.update(dict1))

dict1 = {'a': 1, 'b': 88}
dict2 = {'d': 3, 'c': 4}

print(Merge(dict1, dict2))

print("After merging=" ,dict2)
