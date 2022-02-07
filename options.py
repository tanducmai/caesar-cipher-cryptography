#!/usr/bin/python3

#
# File:         options.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10-Oct-2021
# Description:  Create functions to display the menu driven program, validate
#               user option, and perform actions based on the user option.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


# ------------------------------- Module Import -------------------------------
"""
The random module helps randomise the offset value, hence unpredictable
encryption.
"""
import random


# ---------------------------- Function Definitions ---------------------------
def menu_driven_program():
    print(
        '-------------------',
        '     MAIN MENU',
        '-------------------',
        '1. Enter Message',
        '2. Encrypt Message',
        '3. Decrypt Message',
        '4. Quit',
        sep='\n',
        end='\n\n',
    )


def validate_option():
    """Prompt the user for a number and validate it.

    Returns
    -------
    int
        The valid guess taken from the user.
    """
    option = None

    while option is None or option not in range(1, 5):
        try:
            option = float(input('Enter an option (1,2,3,4): '))
            if option not in range(1, 5):
                print('Invalid choice: option should be between 1 and 4.')
        except ValueError as e:
            print(f'Invalid choice: {e}.')

    return int(option)


def option_1():
    """Prompt for and display the user message to the screen.

    Returns
    -------
    str
        The message received from the user.
    """
    message = input('Please enter a new message: ')
    if message != '':
        print(f'Your message is: \'{message}\'.', end='\n\n')
    else:
        print()
    return message


def option_2(message):
    """Encrypt the user message (no encryption if message is empty)

    Parameters
    ----------
    str
        Original message received from the user, could be empty if the user
        chooses this option before the first one.
    Returns
    -------
    str
        The message that has been successfully encrypted.
    """
    if message == '':
        print('Error: Cannot encrypt an empty message.', end='\n\n')
        return ''
    else:
        offset = random.randint(32, 126)
        encrypted_message = ''
        for i in message:
            unicode_value = ord(i) + offset
            while unicode_value > 126:
                unicode_value -= 95
            encrypted_message += chr(unicode_value)
        encrypted_message += chr(offset)
        print('Your message was successfully encrypted.')
        print(f'Your message is: \'{encrypted_message}\'.', end='\n\n')
        return encrypted_message


def option_3(encrypted_message):
    """Decrypt the user message (no decryption if message is empty)

    Parameters
    ----------
    str
        The message that has been encrypted, could be empty if the user chooses
        this option before the first one.
    Returns
    -------
    str
        The message that has been successfully decrypted.
    """
    if encrypted_message == '':
        print('Error: Cannot decrypt an empty message.', end='\n\n')
        return ''
    else:
        offset = ord(encrypted_message[-1])
        decrypted_message = ''
        for i in encrypted_message:
            unicode_value = ord(i) - offset
            while unicode_value < 32:
                unicode_value += 95
            decrypted_message += chr(unicode_value)
        print('Your message was successfully decrypted.')
        print(f'Your message is: \'{decrypted_message[:-1]}\'.', end='\n\n')
        return decrypted_message[:-1]
