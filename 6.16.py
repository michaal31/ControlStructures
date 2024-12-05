###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0

jt= 40
ut = 70
st = 20
extra_rinse_time = 15
extra_spin_time = 9

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
if program =='j':
    total_washing_time += jt
elif program =='u':
    total_washing_time += ut
elif program == 's':
    total_washing_time += st
else:
    print('Wybierz tryb pralki')
if extra_rinse == 'y':
    total_washing_time += extra_rinse_time
if extra_spin == 'y':
    total_washing_time += extra_spin_time
print(f'Całkowity czas prania: {total_washing_time}.')

