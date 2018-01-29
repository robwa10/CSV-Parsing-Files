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
def items(a_list, *args):
    return_dict = False
    results = 1000
    foo = Counter(a_list)
    if len(args) != 0:
        if len(args) > 2:
            return print('Error: You entered too many params in items().')
        else:
            for i in args:
                if type(i) == int:
                    results = i
                elif type(i) == bool:
                    return_dict = True
    if return_dict is True:
        new_dict = {}
        for value, count in foo.most_common(results):
            new_dict[count] = value
        return new_dict
    else:
        new_list = []
        for value, count in foo.most_common(results):
            new_list.append("%s: %r" % (count, value))
        return new_list


# Parsing----------------------------------------------------------------------
def parse_csv(a_file, s='\n', d=','):
    parsed = []
    f = open(a_file, 'r').read()
    rows = f.split(s)
    for i in rows:
        new = i.split(d)
        parsed.append(new)
    return parsed


def pull(a_list, column):
    new_list = []
    for i in a_list:
        if i[n] != '':
            new_list.append(i[n])
        else:
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
