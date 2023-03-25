# Define variables
total_sum = 0
numbers_to_sum = [i for i in range(10) if i % 2 == 0]

# Calculate the sum of the even numbers
for i, num in enumerate(numbers_to_sum):
    total_sum += num
    if i < len(numbers_to_sum) - 1:
        print(num, end=" + ")
    else:
        print(num, end=" = ")
        
# Display the result
print(total_sum)

# --------------------
# sum=0
# for i in range(0,10):
#     if i%2==0:
#         sum = sum+i
#         print(i,end=" + " )
    
# print("=" , sum)
