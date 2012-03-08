import sys

from abbr import load

# produces dict file for pidgin from abbr.txt

abbr = load(sys.argv[1])

for k, v in abbr.items():
    print """
COMPLETE 1
CASE 0
BAD %s
GOOD %s

""" % (k, v)
