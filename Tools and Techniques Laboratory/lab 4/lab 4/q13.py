
test_str = 'Hello how are you i am fine'

print("The original string is : " + str(test_str))

lookp_dict = {"are" : "replaced1", "fine" : "replaced2"}

temp = test_str.split()
res = []
for wrd in temp:
	
	res.append(lookp_dict.get(wrd, wrd))
	
res = ' '.join(res)

print("Replaced Strings : " + str(res))
