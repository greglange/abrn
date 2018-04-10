import re
import sys
import urllib2

import abbr

abs = dict([[x[1], x[0]] for x in abbr.load(sys.argv[1]).items()])

url = 'http://www.edict.com.hk/lexiconindex/frequencylists/words2000.htm'

content = urllib2.urlopen(url)

pattern = re.compile('target="Vocabulary">(.+?)</a>')

for line in content.readlines():
    match = pattern.search(line)

    if match:
        word = match.group(1).lower()

        if not abs.has_key(word):
            abs[word] = '_'

for k, v in sorted(abs.iteritems()):
    print '%s\t%s' % (v, k)
