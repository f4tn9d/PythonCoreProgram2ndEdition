#!/usr/bin/python

'makeNReadTextFile.py -- choose to create, read or edit text file'

import os
import curses
ls=os.linesep
while True:
    print """
    ##############################
    ##  There's a menu:
    ##    1.create a text file.
    ##    2.read a text file.
    ##    3.edit a text file.
    ##    4.exit.
    ##############################
        """
    c = int(raw_input("Pls choose a choice to do: "))
    if c == 1:
        fname = raw_input("Pls input a filename: ")
        try:
            fobj = open(fname, 'w')
        except IOError, e:
            print "*** file open error: ", e
        else:
            all = []
            print "\nEnter lines('.' by itself to quit).\n"
            while True:
                entry = raw_input('> ')
                if entry == '.':
                    break
                else:
                    all.append(entry)
            fobj.writelines(['%s%s' % (x, ls) for x in all])
            fobj.close()
        print 'DONE!'
    if c == 2:
        fname = raw_input("Pls input a filename: ")
        try:
            fobj = open(fname, 'r')
        except IOError, e:
            print "*** file open error: ", e
        else:
            print "The content of file '%s' is: " % fname
            for eachLine in fobj:
                print eachLine.strip('\n')
            fobj.close()
        print 'DONE!'
    if c == 3:
        fname = raw_input("Pls input a filename: ")
        try:
            fobj = open(fname, 'w')
        except IOError, e:
            print "*** file open error: ", e
        else:
            print 
    if c == 4:    
        break
