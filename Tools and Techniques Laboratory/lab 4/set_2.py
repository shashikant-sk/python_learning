# Python | Convert set into a list

# original
# Python3 program to convert a
# set into a list
my_set = {'Geeks', 'for', 'geeks'}

s = list(my_set)
print(s)

# -------------------------
# modifed

def convert(set):
	return list(set)

# Driver function
s = set({1, 2, 3})
print(convert(s))

