#Write a program that calculates a dog's age in dog's years. 
# For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years


human_yeasrs = float(input('Enter the dogs age in human years: '))
if human_yeasrs <= 2:
    dog_years = human_yeasrs * 10.5
else: 
    dog_years = 2 * 10.5 + (human_yeasrs -2 ) * 4
print(f'The dogs age in dogs years is {dog_years:.0f} years')