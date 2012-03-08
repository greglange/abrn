import sys

from abbr import load

# produces completions portion of config file for irssi from abbr.txt

abbr = load(sys.argv[1])

print "completions = {"

for k, v in abbr.items():
    print """  %s  = { value = "%s"; auto = "yes"; };""" % (k, v)

print "};";
