"""
  Counts the instances of each item in a list using `Counter`.

  @since 1.0.0
  @category: Parsing
  @param (list) a_list: The list to count.
  @param (boolean) [optional] dict=False: Boolean to return
      list (default) or dictionary. Must be passed if an int is passed as
      third param.
  @param (int) [optional] n=1000: Integer to limit data returned.
      Default is 1000.
  @returns (list) [default]: Returns a list.
    Each item in the list is `[occurrence total: 'value']`.
    (Dictionary) [optional]: Returns a dictionary.
    Key, value pairs are `{occurrence total: 'value'}`.

  @example
  data = [a, v, a, f, d, b, d, f, d, b, d, a, f, a, a]
  results = items(data)
  limit_results = items(data, 3)
  dict_limit_results = items(data, True, 3)

  print(results)
  print(limit_results)
  print(dict_limit_results)
  // ["5: 'a'","4: 'd'", "3: 'f'", "2: 'b'",  "1: 'v'"]
  // ["5: 'a'","4: 'd'", "3: 'f'"]
  // {5: 'a', 4: 'd', 3: 'f'}
"""


# Imported Modules
from collections import Counter


def items(a_list, dict=False, results=1000):
    # Count occurenences in the list.
    foo = Counter(a_list)
    # Check if default list should be returned.
    if dict is False:
        new_list = []
        for value, count in foo.most_common(results):
            new_list.append("%s: %r" % (count, value))
        return new_list
    # Return dictionary instead of list.
    else:
        new_dict = {}
        for value, count in foo.most_common(results):
            # Make total count the key, which is the reverse of Counter.
            new_dict[count] = value
        return new_dict
