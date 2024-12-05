# Write a program that prints a lottery coupon (numbers from 1 to 49) 

for i in range(7):
    for j in range(7):
        num = i + 1 + j * 7
        print(num, end=' ')
    print()
