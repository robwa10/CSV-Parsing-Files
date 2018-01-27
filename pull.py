def pull(a_list, n):
    new_list = []
    for i in a_list:
        if i[n] != '':
            new_list.append(i[n])
        else:
            x = n - 1
            new_list.append('Column was blank.')
    return new_list
