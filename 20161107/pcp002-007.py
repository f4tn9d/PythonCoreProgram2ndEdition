#!/usr/bin/python
#-*- coding=utf-8 -*-

print 'Using while to cpl:'
s=raw_input('Pls input a string:')
i=0
while i<(len(s)):
    print s[i],
    i+=1
print


print 'Using for to cpl:'
for j in s:
    print j,
print
