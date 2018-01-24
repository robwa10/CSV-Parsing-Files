# Imported modules
from collections import Counter
import reprlib

def parse_csv(a_file):
    """Pass in a csv file to be read and split on newline and comma
    then added to a list."""
    parsed = []
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        new = i.split(',')
        parsed.append(new)
    return parsed


def pull_items(a_list, n):
    """Pass in a list and column number.
    Returns new list with items from specified column."""
    new_list = []
    for i in a_list:
        if i[n] != '':
            new_list.append(i[n])
        else:
            x = n - 1
            new_list.append('Column was blank.')
    return new_list


def count_items(a_list, n=1000):
    """Counts items in list and returns a list formatted for print()."""
    print_list = ['Total: Reason']
    foo = Counter(a_list)
    # n can be passed to limit the amount of items returned in the list.
    # For example pass 10 to see only the top 10 items.
    for value, count in foo.most_common(n):
        print_list.append("%s: %r" % (count, value))
    return print_list


def count_to_dict(a_list):
    """Count items in list and return dict with number of each occurance as key."""
    new_dict = {}
    foo = Counter(a_list)
    for value, count in foo.most_common():
        new_dict[count] = value
    return new_dict
