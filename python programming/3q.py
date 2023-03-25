total_sum = 0

for i in range(0, 10):
    if i % 2 == 0:
        total_sum += i
        if i == 0: # if i is 0, we don't want to print the + sign before it 
            print(i, end="")
        else:
            print(f" + {i}", end="") # f string is used to format the string example f" + {i}" is same as " + " + str(i)
        
print(" = ", total_sum)