# Original - Python program to interchange first and last elements in a list
# Edit - WAP to reverse a list by swapping mirror elements
lis = list(map(int, input('Enter list elements: ').split()))
print(f"Initial list -> {lis}")
for i in range(len(lis) // 2):
    temp = lis[i]
    lis[i] = lis[len(lis) - i - 1]
    lis[len(lis) - i - 1] = temp
print(f"Reversed list -> {lis}")