#!/usr/local/bin/python

from __future__ import unicode_literals
#from __future__ import division

import sys

print 'Hello, this is the third python project.'

print 'The version of this python is:', sys.version

print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is unicode?', isinstance('xxx', unicode)

print '10/3=', 10/3
print '10.0/3=', 10.0/3
