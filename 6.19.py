#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n): n
#Do you have an Instagram account? (y/n): y

#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

interested_in_computer_science = input("Are you interested in computer science? (y/n): ")
like_playing_computer_games = input("Do you like playing computer games? (y/n): ")
has_instagram_account = input("Do you have an Instagram account? (y/n): ")
    
print('RESULTS')
if interested_in_computer_science == 'y':
    print(f'Interested in computer science: yes')
else :
    print('Interested in computer science: No')
if like_playing_computer_games == 'y':
    print('Playing computer games: yes')
else: 
    print('Playing computer games: no')
if has_instagram_account =='y':
    print('Has an Instagram account: yes')
else:
    print('Has an Instagram account: no')

