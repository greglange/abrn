def load(filename):
    abbr = {}
    for line in [x.rstrip() for x in open(filename, 'r')]:
        a = line.split("\t")
        if a[0] in ('_', 'xxx'):
            continue

        if abbr.has_key(a[0]):
            raise Exception("Duplicate abbreviation '%s' found" % (a[0]))

        abbr[a[0]] = a[1]

    return abbr
