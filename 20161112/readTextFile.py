#!/usr/bin/python

'readTextFile.py -- read and display text file'

fname = raw_input('Enter filename: ')
print "The content of file '%s' is:" % fname

try:
    fobj = open(fname, 'r')
except IOError, e:
    print '*** file open error:', e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()
