
test_dict = {"Gfg" : [5, 7, 5, 4, 5],
			"is" : [6, 7, 4, 3, 3],
			"Best" : [9, 9, 6, 5, 5]}

print("The original dictionary is : " + str(test_dict))

max_val = 0
max_key = None
for sub in test_dict:
	
	if len(set(test_dict[sub])) > max_val:
		max_val = len(set(test_dict[sub]))
		max_key = sub

print("Key with maximum unique values : " + str(max_key))
