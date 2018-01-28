"""
All commenting has been removed from the code contained within this module.
Each function contains it's own file with exstensive commenting.

Sections and functions are listed alphabetically.

For full documentation please see:
https://github.com/robwa10/Parse-and-Analyze

Copyright 2018 Robert Hubbard
Licensed under the MIT License
"""


# Imported Modules
from collections import Counter


# Counting---------------------------------------------------------------------
def items(a_list, n=1000, x=False):
    foo = Counter(a_list)
    if x is False:
        new_list = []
        for value, count in foo.most_common(n):
            new_list.append("%s: %r" % (count, value))
        return new_list
    else:
        new_dict = {}
        for value, count in foo.most_common(n):
            new_dict[count] = value
        return new_dict


# Parsing----------------------------------------------------------------------
def parse_csv(a_file, s='\n', d=','):
    parsed = []
    f = open(a_file, 'r').read()
    rows = f.split(s)
    for i in rows:
        new = i.split(d)
        parsed.append(new)
    return parsed


def pull(a_list, n):
    new_list = []
    for i in a_list:
        if i[n] != '':
            new_list.append(i[n])
        else:
            x = n - 1
            new_list.append('Column was blank.')
    return new_list


# Validation-------------------------------------------------------------------
def present_choices(choices):
    print('Please choose one.')
    for i in choices:
        print(i)
    user_input = input('> ').lower()
    return user_input


def validate_choice(choices=[]):
    if len(choices) == 0:
        choices = ['Yes', 'No']
    lowercase_list = []
    for i in choices:
        lowercase_list.append(i.lower())
    their_choice = present_choices(choices)
    while their_choice not in lowercase_list:
        print('Invalid Input.')
        their_choice = present_choices(choices)
    return their_choice
