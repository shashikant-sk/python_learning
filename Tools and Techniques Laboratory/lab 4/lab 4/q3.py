list1 = [9, 8, 4, 5, 6, 7, 10, 3, 1, 2]

even_count, odd_count = 0, 0

for num in list1:

	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
