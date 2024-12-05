# Determine the age group based on user input:
# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older


age = int(input("Enter your age: "))

if age < 13:
    age_group = "Child"
elif 13 <= age <= 19:
    age_group = "Teen"
elif 20 <= age <= 64:
    age_group = "Adult"
else:
    age_group = "Senior"

print(f"Your age group: {age_group}")
