#!/usr/bin/python
#-*- coding=utf-8 -*-
print "Use for to solve this prolem:"
sf = 0
for i in range(0, 5):
    af = range(5)
    af[i] = (int(raw_input('Pls input an integer:')))
    sf += af[i]
print "The sum is:",
print sf

print "Use while to solve this prolem:"
sw = 0
j = 0
aw=range(5)
while j < len(aw):
    aw[j] = (int(raw_input('Pls input an integer:')))
    sw += aw[j]
    #Must remember this j should be added one every time
    j += 1
print "The sum is:",
print sw
