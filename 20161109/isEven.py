#!/usr/bin/python
#-*- coding=utf-8 -*-

def isEven(a):
    if a < 0:
        print "U have input the wrong number!Pls try again."
    elif a == 0:
        return "True"
    elif a == 1:
        return "False"
    else:
        return isEven(a-2)
