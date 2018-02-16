"""
Counts the instances of each item in a list using `Counter`.

Since:
    1.0.0

Category:
    Parsing

Args:
    param1 (list) a_list: The list to count.
    param2 (boolean) [optional] dict=False: Boolean to return
        list (default) or dictionary. Must be passed if an int is passed as
        third param.
    param3 (int) [optional] n=1000: Integer to limit data returned.
        Default is 1000.

Returns:
    list: Each item in the list is `[occurrence total: 'value']`.
    dictionary: [optional]: Key, value pairs are `{occurrence total: 'value'}`.

Example:
    >>> data = ['a', 'v', 'a', 'f', 'd', 'b', 'd', 'f',
        'd', 'b', 'd', 'a', 'f', 'a', 'a']
    >>> print(items(data))
    ["5: 'a'", "4: 'd'", "3: 'f'", "2: 'b'",  "1: 'v'"]
    >>> print(items(data, 3))
    ["5: 'a'", "4: 'd'", "3: 'f'"]
    >>> print(items(data, True, 3))
    {5: 'a', 4: 'd', 3: 'f'}
"""


# Imported Modules
from collections import Counter


def items(a_list, *args):
    return_dict = False
    results = 1000
    # Count occurenences in the list.
    foo = Counter(a_list)
    # Check for optional params.
    if len(args) != 0:
        # If more than 2 params entered return error message.
        if len(args) > 2:
            return print('Error: You entered too many params in items().')
        else:
            # Check param type and change appropriate function variable.
            for i in args:
                if type(i) == int:
                    results = i
                elif type(i) == bool:
                    return_dict = True
    # Return dictionary instead of list.
    if return_dict is True:
        new_dict = {}
        for value, count in foo.most_common(results):
            # Make total count the key, which is the reverse of Counter.
            new_dict[count] = value
        return new_dict
    # Check if default list should be returned.
    else:
        new_list = []
        for value, count in foo.most_common(results):
            new_list.append("%s: %r" % (count, value))
        return new_list
