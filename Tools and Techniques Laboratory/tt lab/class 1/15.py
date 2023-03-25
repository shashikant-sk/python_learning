# Input marks and display grade according to KIIT University
mark = int(input("Enter total marks: "))
if mark >= 90:
    print("O grade")
elif mark >= 80:
    print("E grade")
elif mark >= 70:
    print("A grade")
elif mark >= 60:
    print("B grade")
elif mark >= 50:
    print("C grade")
elif mark >= 40:
    print("D grade")
else:
    print("F grade")