amt=0
nu=int(input("Enter number of electric unit"))
if nu<=100:
    amt=0
elif nu>100 and nu<=200:
    amt=(nu-100)*5
else:
    amt=500+(nu-200)*10
print("Amount to pay :",amt)