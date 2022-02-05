# Syntax  of nested-if statements

# if (condition1):
#     #executes if condition1 is True 
#     if (condition2):
#         #executes if condition 2 is true 
#     #condition2 end here
# #condition1 end here


c = 21
if c<25:
    if c%2==0:
        print("C is an even number less than 25")
    else:
        print("c is an odd number less than 25")
else:
    print("c is greater than 25")