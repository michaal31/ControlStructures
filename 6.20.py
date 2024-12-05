#Sample result:

#Enter decimal number: 12
#12(10) = 1100(2)

decimal_number = int(input("Enter decimal number: "))
if decimal_number == 0:
    print("0(10) = 0(2)")
remainders = []

while decimal_number > 0:
    remainder = decimal_number % 2
    remainders.append(str(remainder))
    decimal_number = decimal_number // 2
binary_number = ''.join(remainders[::-1])
print(f"{decimal_number} (10) = {binary_number} (2)")



