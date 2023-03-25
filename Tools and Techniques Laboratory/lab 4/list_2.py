# Python – Swap elements in String list

# original


test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']


print("The original list is : " + str(test_list))

# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

print ("List after performing character swaps : " + str(res))

# ----------------------
# modifed

import re //  #support for regular expressions

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("The original list is : " + str(test_list))
# using regex
res = [re.sub('-', 'e', re.sub('e', 'G', re.sub('G', '-', sub))) for sub in test_list]
# printing result
print("List after performing character swaps : " + str(res))





