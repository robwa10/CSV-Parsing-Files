"""
  Creates a list from data within each row of a CSV file
  and appends that list to a list.

  @since 1.0.0
  @category: Parsing
  @param (file) a_file - The CSV to be parsed.
  @param (string) [optional] s: The character that splits rows.
  @param (string) [optional] d: The character that splits data within each row.
  @returns (list of lists): Returns a list of lists.

  @example
  parsed_data = parse_csv('data.csv')

  print(parsed_data)
  // [[John, Smith, jsmith@email.com], [Jane, Doe, jane@email.com]]
"""


def parse_csv(a_file, s='\n', d=','):
    parsed = []
    # Open CSV in read mode.
    f = open(a_file, 'r').read()
    # Split the CSV rows.
    rows = f.split(s)
    # Iterate over rows and add individual data to parsed as a list.
    for i in rows:
        new = i.split(d)
        parsed.append(new)
    return parsed
