#!/usr/bin/python
#-*- coding=utf-8 -*-

'display the type of sth'

def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!!'

displayNumType(-69)
displayNumType(99999999999999999999999)
displayNumType(98.6)
displayNumType('xxx')
