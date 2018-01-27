def parse_csv(a_file, s='\n', d=','):
    parsed = []
    f = open(a_file, 'r').read()
    rows = f.split(s)
    for i in rows:
        new = i.split(d)
        parsed.append(new)
    return parsed
