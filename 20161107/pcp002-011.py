#!/usr/bin/python
#-*- coding=utf-8 -*-

while True:
    print """
    1.get the sum
    2.get the avg
    x.quit
    Pls make your choice:""",
    s=raw_input()
#You should put string check on the 1st one.
    if s == "x":
        break
#Other conditions should be considered also.
    elif s != "1" and s != "2":
        print "You've a wrong input!!!Input again PLS~"
    elif int(s) == 1:
        print "We'll get the sum of 5 numbers."
    elif int(s) == 2:
        print "We'll get the avg of 5 numbers."
    else:
        print "You've a wrong input!!!Input again PLS~"
