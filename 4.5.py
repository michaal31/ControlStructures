###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    if char.isalpha():
        char_code = ord(char)
    # add one to the character's code
        if char.islower():
            char_code = ord('a') + (char_code - ord('a') + 1) % 26
        elif char.isupper():
            char_code = ord('A') + (char_code - ord('A') + 1) % 26
    # replace new character code with its
    # corresponding character (use chr())
        encrypted_char = chr(char_code)
    else:
        encrypted_char = char
    # add encrypted character to encrypted text
    encrypted_text += encrypted_char

print(plain_text)
print(encrypted_text)
    