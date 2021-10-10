#!/usr/bin/env python3

#
# File:         options.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10/10/2021
# Description:  Create functions to perform actions based on the user option.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


import random


def option_1(message):
    message = input('Please enter a new message: ')
    print(f'Your message is: \'{message}\'')
    return message

def option_2(message):
    if message == '':
        print('Error: Cannot encrypt an empty message.')
        return None
    else:
        OFFSET = random.randint(32, 126)
        encrypted_message = ''
        for i in message:
            UNICODE_VALUE = ord(i) + OFFSET
            while UNICODE_VALUE > 126:
                UNICODE_VALUE -= 95
            encrypted_message += chr(UNICODE_VALUE)
        encrypted_message += chr(OFFSET)
        print('Your message was successfully encrypted.')
        print(f'Your message is: \'{encrypted_message}\'')
        return encrypted_message

def option_3(message):
    if message == '':
        print('Error: Cannot decrypt an empty message.')
        return None
    else:
        OFFSET = ord(message[-1])
        decrypted_message =''

        print('Your message was successfully decrypted.')
        print(f'Your message is: \'{decrypted_message}\'')
        return decrypted_message





