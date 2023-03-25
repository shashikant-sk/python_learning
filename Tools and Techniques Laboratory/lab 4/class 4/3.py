# Original - Python program to find all positive numbers in a list
# Edited - WAP to find all positive, negative and zeroes in a list
lis = list(map(int, input('Enter list elements: ').split()))
pos = []
neg = []
zeros = []
print(f"Initial list -> {lis}")
for i in lis:
    if i > 0:
        pos.append(i)
    elif i < 0:
        neg.append(i)
    else:
        zeros.append(i)
print(f"Positive list -> {pos}")
print(f"Negative list -> {neg}")
print(f"Zeroes list -> {zeros}")
