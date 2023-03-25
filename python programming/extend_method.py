# what if we don't want to add a single element to the end of the list but an entire list to the end of the list? Well, we can use the extend method for that. The extend method is used as follows:

num = [1,2,3,4]
print(num)
 
num1 = [5,6,7,8]
num.extend(num1) #--> it add the list in the last of the list
print(num)

# similarly we can use the insert method to add an element to a specific index in the list. The insert method is used as follows:
# and we can also add string in the list and extend the list
# num = [1,2,3,4]
# print(num)
# stg=["hello","world"]
# num.extend(stg)
# print(num)
