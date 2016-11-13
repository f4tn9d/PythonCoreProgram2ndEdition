#!/usr/bin/python

'makeTextFile.py -- create text file, use a different way to check errors.'

import os
ls=os.linesep
fname = raw_input("Pls input a filename: ")
try:
    fobj = open(fname, 'w')
except IOError, e:
    print "\n*** file open error:", e
else:    
    all = []
    print "\nEnter lines('.' by itself to quit). \n"
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

        fobj.writelines(['%s%s' % (x, ls) for x in all])
        fobj.close()
    print 'DONE!'
