# WAP to display the following style o/p for a given string input through keyboard.
# (Ex.for a string "KIITCSIT")
# KIITCSITTISCTIIK
# KIITCSI  ISCTIIK
# KIITCS    SCTIIK
# KIITC      CTIIK
# KIIT        TIIK
# KII          IIK
# KI            IK
# K              K
# KI            IK
# KII          IIK
# KIIT        TIIK
# KIITC      CTIIK
# KIITCS	SCTIIK
# KIITCSI  ISCTIIK
# KIITCSITTISCTIIK
s = input("Enter the string: ")
for i in range(len(s)):
    newS = s[:len(s) - i]
    print(newS, end='')
    for j in range(2 * i):
        print(end=' ')
    newS = ''.join(reversed(newS))
    print(newS)
for i in range(1, len(s)):
    newS = s[:i + 1]
    print(newS, end='')
    for j in range(2 * (len(s) - i) - 2):
        print(end=' ')
    newS = ''.join(reversed(newS))
    print(newS)

