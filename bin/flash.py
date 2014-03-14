import sys

from abbr import load

abbr = load(sys.argv[1])

files = [
    ['1_2.flash', lambda x: len(x) < 3],
    ['3_l.flash', lambda x: len(x) == 3 and x[0] <= 'l'],
    ['3_m.flash', lambda x: len(x) == 3 and x[0] >= 'm'],
    ['4_5_l.flash', lambda x: len(x) >= 4 and x[0] <= 'l'],
    ['4_5_m.flash', lambda x: len(x) >= 4 and x[0] >= 'm'],
]

for f in files:
    fd = open(f[0], 'w')
    for k, v in abbr.items():
        if f[1](k):
            fd.write('%s\t%s\n' % (k, v))
            fd.write('%s\t%s\n' % (v, k))
    fd.close()
