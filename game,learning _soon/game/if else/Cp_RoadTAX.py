tax = 0
cp=float(input("Enter Your Bike Cost cpice"))
if cp > 100000:
    tax = 15/100*cp
elif cp > 50000:
    tax = 10/100*cp
else:
    tax = 5/100*cp
    print("TAX to paid is ::",tax)
    