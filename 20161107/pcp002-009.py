#!/usr/bin/python
#-*- coding=utf-8 -*-
sf = 0
for i in range(0, 5):
    af = range(5)
    af[i] = (int(raw_input('Pls input an integer:')))
    sf += af[i]
print "The avg is:",
print float(sf)/float(len(af))

