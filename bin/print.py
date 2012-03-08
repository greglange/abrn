import sys

from abbr import load

abbr = load(sys.argv[1])

# print abbreviations sorted by expansions
for k, v in sorted(abbr.iteritems(), key=lambda (k, v): (v, k)):
    print "     %s %s" % (k.rjust(5), v)
