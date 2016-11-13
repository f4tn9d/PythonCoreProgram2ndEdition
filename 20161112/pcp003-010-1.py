#!/usr/bin/python

'readTextFile.py -- read file content, use os.path.exists() to check errors.'
import os

fname = raw_input('Enter filename: ')
if os.path.exists(fname):
    print "The content of file '%s' is:" % fname

    fobj = open(fname, 'r')
    for eachLine in fobj:
        print eachLine,
    fobj.close()
else:
    print "\nFile '%s' doesn't exist!" % fname
