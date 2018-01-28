"""
  Counts the instances of each item in a list using `Counter`.

  @since 1.0.0
  @category - Parsing
  @param (list) a_list: The list to count.
  (int) [optional] n=1000: Integer to limit data returned. Default is 1000.
  (boolean) [optional] x=False: Boolean to return list (default) or dictionary.
  @returns (list) [default]: Returns a list.
    Each item in the list is `[occurrence total: 'value']`.
    (Dictionary) [optional]: Returns a dictionary.
    Key, value pairs are `{occurrence total: 'value'}`.

  @example
  data = [a, v, a, f, d, b, d, f, d, b, d, a, f, a, a]
  results = items(data)
  limit_results = items(data, 3)
  limit_results = items(data, 3, True)
  
  print(results)
  print(limit_results)
  // ["5: 'a'","4: 'd'", "3: 'f'", "2: 'b'",  "1: 'v'"]
  // ["5: 'a'","4: 'd'", "3: 'f'"]
  // {5: 'a', 4: 'd', 3: 'f'}
"""


# Imported Modules
from collections import Counter


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
