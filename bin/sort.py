import sys

fd = open(sys.argv[1])

items = {}
for line in fd:
    line = line.strip()
    v, k = line.split('\t')

    if k in items:
        print "duplicate expansion found '%s'" % (k)
        sys.exit()

    items[k] = v

for k, v in sorted(items.iteritems()):
    print '%s\t%s' % (v, k)
