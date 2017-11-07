data = dict()
for line in open('abbr.txt'):
    line = line.strip()

    row = line.split()

    if row[0] == 'xxx':
        continue

    data[row[0]] = row[1]


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)

for a in char_range('a', 'z'):
    if a not in data:
        print a
    for b in char_range('a', 'z'):
        if a + b not in data:
            print a + b
        for c in char_range('a', 'z'):
            if a + b + c not in data:
                print a + b + c
            for d in char_range('a', 'z'):
                if a + b + c + d not in data:
                    print a + b + c + d
