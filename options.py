#!/usr/bin/env python3

#
# File:         options.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10/10/2021
# Description:  Create functions to perform actions based on the user option.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


def option_1(message):
    message = input('Please enter a new message: ')
    print(f'Your message is: \'{message}.\'')
    return message