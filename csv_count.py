# Imported modules
from collections import Counter
import reprlib

# Customize the limits for reprlib
r = reprlib.Repr()
r.maxstring = 40
r.maxlist = 10

# Global variables
parsed = []
list_items = []


def prep_file(a_file):
    """Read and split the csv on newline and comma and add to a list."""
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        new = i.split(',')
        parsed.append(new)


def pull_items(a_list, n):
    """Put items from specified column into a list."""
    for i in a_list:
        list_items.append(i[n])


def print_items(x):
    """Count items and print a formatted list."""
    print_list = []
    foo = Counter(x)
    for value, count in foo.most_common():
        print_list.append("%s occured %r times." % (r.repr(value), count))
    print("\n".join(print_list))


data_file = input("Please enter a file. > ")
data_column = int(input("Column to be counted? e.g.[1,2,3...] > ")) - 1
prep_file(data_file)
pull_items(parsed, data_column)
print_items(list_items)
