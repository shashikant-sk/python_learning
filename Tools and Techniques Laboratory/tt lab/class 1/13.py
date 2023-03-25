# Input a alphabet, convert to it lowercase and return
ch = input("Enter alphabet: ")
ch = ord(ch)
if ch >= 65 and ch <= 90:
    print(chr(ch + 32))
elif ch >= 97 and ch <= 122:
    print(chr(ch))
else:
    print("Not a letter.")