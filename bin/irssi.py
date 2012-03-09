import sys

from abbr import load

# produces completions portion of config file for irssi from abbr.txt

abbr = load(sys.argv[1])

print "completions = {"

abbrs = abbr.items()
abbrs.sort(key=lambda kv: '%s%s' % (len(kv[0]), kv[0]))
for k, v in abbrs:
    print """  %s  = { value = "%s"; auto = "yes"; };""" % (k, v)

print "};";
