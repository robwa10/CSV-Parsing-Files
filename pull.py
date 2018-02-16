"""
Pass in data from `parsed_csv()` and a column index.
Creates a list with data from index.
Catches empty columns.

Since:
    1.0.0

Category:
    Parsing

Args:
    param1 (list) a_list: A list of lists.
    param2 (int) column: index of a column in CSV.

Returns:
    list of lists: Returns a list.

Example:
    >>> parsed_data = parse_csv('data.csv')
    >>> email = pull(parsed_data, 2)
    >>> print(email)
    [jsmith@email.com, jane@email.com]
"""


def pull(a_list, column):
    new_list = []
    # Iterate of the rows from the CSV.
    for i in a_list:
        # Add contents of cell from specified column to a list.
        if i[n] != '':
            new_list.append(i[n])
        # If the cell is blank catch it.
        else:
            new_list.append('Column was blank.')
    return new_list
