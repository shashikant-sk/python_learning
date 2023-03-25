# Find average marks and percentage of a student in 5 subjects
marks = list(map(int, input("Enter marks in 5 subjects: ").split()))
sum = 0
for mark in marks:
    sum += mark
print(f"Average = {sum / 5}")
print(f"Percentage = {sum / 5}%")
