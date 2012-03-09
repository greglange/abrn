import sys

from abbr import load

# produces completions portion of config file for irssi from abbr.txt

abbr = load(sys.argv[1])

print "completions = {"

for k, v in sorted(abbr.items(), key=lambda (k, v): (len(k), k)):
    print """  %s  = { value = "%s"; auto = "yes"; };""" % (k, v)

print "};";
