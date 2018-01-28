"""
  Pass in data from `parsed_csv()` and a column index.
  Creates a list with data from index.
  Catches empty columns.

  @since 1.0.0
  @category - Parsing
  @param (list) a_list: A list of lists.
  @param (int) n: index of a column in CSV.
  @returns (list of lists): Returns a list.

  @example
  parsed_data = parse_csv('data.csv')
  email = pull(parsed_data, 2)
  
  print(email)
  // [jsmith@email.com, jane@email.com]
"""


def pull(a_list, n):
    new_list = []
    for i in a_list:
        if i[n] != '':
            new_list.append(i[n])
        else:
            x = n - 1
            new_list.append('Column was blank.')
    return new_list
