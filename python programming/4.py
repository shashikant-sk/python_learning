total_sum=0
for i in range(0,10):
    if i % 2 == 0:
        total_sum += i
        if i==0:
            print(i,end="")
        else :
            print(f" + {i}",end="")
print(" = ", total_sum)