#!/usr/bin/python
#-*- coding=utf-8 -*-

while True:
    a = int(raw_input('Pls input an integer between 1-100:'))
    if a > 0 and a < 101:
        print "Successfully input!!!"
        break
    print "Have input the wrong number!!!"
