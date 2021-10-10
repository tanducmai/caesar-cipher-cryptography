#!/usr/bin/env python3

#
# File:         encryption.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10/10/2021
# Description:  Use Caesar Cipher technique to encrypt or decrypt an inputted message.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


import options


menu_driven_program = (
"""
-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit
"""
)

print(menu_driven_program)
message = ''
option = int(input('Enter an option (1,2,3,4): '))

# Input Validation.
while option not in range(1, 5):
    option = int(input('Invalid choice. Enter an option (1,2,3,4): '))

# Now we have a valid option.
while option != 4:
    if option == 1:
        message = options.option_1(message)
    elif option == 2:
        print('Option 2: Encrypt Message')
        options.option_2(message)
    else:
        print('Option 3: Decrypt Message')
    print(menu_driven_program)
    option = int(input('Enter an option (1,2,3,4): '))

# Exit the loop, meaning option == 4:
print(f'Your message is: \'{message}.\'')
print('\nGoodbye')
