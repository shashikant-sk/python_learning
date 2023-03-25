# Check if character enter through keyboard is a letter digit or special character
ch = input("Enter a character: ")
if ch >= '1' and ch <= '9':
    print("Digit")
elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print("Letter")
else:
    print("Special Character")