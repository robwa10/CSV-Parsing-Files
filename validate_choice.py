"""
Presents the user with a selection of choices and validates their input.
Defaults to Yes or No selection if called with no argument.

Since:
    1.0.0

Category:
    Validation

Args:
    param (list) [optional] choices: List of choices for user to select from.
        Defaults to Yes/No if called with no param.

Returns:
    string: Returns validated input as a lowercase string.

Example:
>>> my_choices = ['Bob', 'Susie', '3', '4']
>>> print(validate_choice(my_choices))
Please choose one.
Bob
Susie
3
4
>>> Bob
bob
"""


def present_choices(choices):
    print('Please choose one.')
    for i in choices:
        print(i)
    user_input = input('> ').lower()
    return user_input

def validate_choice(choices=[]):
    # Check if called with no params for default Yes/No.
    if len(choices) == 0:
        choices = ['Yes', 'No']
    # Lowercase all list items to validate against user input.
    lowercase_list = []
    for i in choices:
        lowercase_list.append(i.lower())
    # Give user choices and ask for input.
    their_choice = present_choices(choices)
    # Validate user input.
    while their_choice not in lowercase_list:
        print('Invalid Input.')
        their_choice = present_choices(choices)
    return their_choice
