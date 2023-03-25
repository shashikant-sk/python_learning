# WAP to convert a binary number to its equivalent octal & hexa-decimal number system.
bin = input("Enter binary: ")
binHex = bin
binOct = bin
hex = ''
oct = ''
hexTable = {'0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'A',
            '1011': 'B',
            '1100': 'C',
            '1101': 'D',
            '1110': 'E',
            '1111': 'F'}
octTable = {'000': '0',
            '001': '1',
            '010': '2',
            '011': '3',
            '100': '4',
            '101': '5',
            '110': '6',
            '111': '7',}
while len(binHex) % 4 != 0:
    binHex = '0' + binHex
while len(binOct) % 3 != 0:
    binOct = '0' + binOct
for ind in range(0, len(binHex), 4):
    conv = binHex[ind] + binHex[ind + 1] + binHex[ind + 2] + binHex[ind + 3]
    hex += hexTable[conv]
for ind in range(0, len(binOct), 3):
    conv = binOct[ind] + binOct[ind + 1] + binOct[ind + 2]
    oct += octTable[conv]

print(f"Hexadecimal: {hex}")
print(f"Octal: {oct}")