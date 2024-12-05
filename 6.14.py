
facebook = True
twitter = False
instagram = True
count = sum([facebook, twitter, instagram])
    
    # Check if the person has at least two accounts
if count >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")


