def load(filename):
    abbr = {}
    for line in [x.rstrip() for x in open(filename, 'r')]:
        a = line.split("\t")
        if a[0] in ('_', 'xxx'):
            continue

        if a[0] in abbr:
            raise Exception("Duplicate abbreviation '%s' found" % (a[0]))

        if len(a) == 2:
            abbr[a[0]] = a[1]

    return abbr
