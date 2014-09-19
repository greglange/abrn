import sys

from abbr import load

abbr = load(sys.argv[1])

files = [
    ['abbr2.txt', lambda x: len(x) < 3],
    ['abbr3.txt', lambda x: len(x) == 3],
    ['abbr4.txt', lambda x: len(x) >= 4],
]

for f in files:
    fd = open(f[0], 'w')
    for k, v in sorted(abbr.items()):
        if f[1](k):
            fd.write('%s\t%s\n' % (k, v))
            fd.write('%s\t%s\n' % (v, k))
    fd.close()
