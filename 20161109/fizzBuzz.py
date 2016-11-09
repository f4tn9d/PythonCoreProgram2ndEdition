#!/usr/bin/python
#-*- coding=utf-8 -*-

for i in range(1,101):
    if i%3==0:
        print ("%6s"%("Fizz")),
    elif i%5==0:
        print ("%6s"%("Buzz")),
    else:
        print ("%6d"%(i)),
    if i%6==0:
        print
