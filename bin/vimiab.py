from sys import argv, exit
from abbr import load

# produces insert-mode abbreviations commands for vim from abbr.txt
if len(argv) != 2:
    exit('''
Syntax: %(prog)s <abbr.txt>

You might do:
%(prog)s <abbr.txt> > ~/.vimiab
echo "map <Leader>a :source ~/.vimiab<CR>" >> ~/.vimrc

Then you can open up a file, hit \a to turn on abbreviation mode, and start
editing.
'''.strip() % {'prog': argv[0]})
for k, v in sorted(load(argv[1]).items(), key=lambda (k, v): (len(k), k)):
    print 'iab %s %s' % (k, v)
