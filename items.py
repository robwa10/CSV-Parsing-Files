from collections import Counter


def items(a_list, n=1000, x=False):
    foo = Counter(a_list)
    if x == False:
        new_list = []
        for value, count in foo.most_common(n):
            new_list.append("%s: %r" % (count, value))
        return new_list
    else:
        new_dict = {}
        for value, count in foo.most_common(n):
            new_dict[count] = value
        return new_dict
