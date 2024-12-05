#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN

hours_parked = int(input("Enter the number of hours parked: "))
if 1 <= hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0
print(f'Parking fee is {fee}')