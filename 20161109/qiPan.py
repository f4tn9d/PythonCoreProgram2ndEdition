#!/usr/bin/python
#-*- coding=utf-8 -*-

#sz = 8
sz=int(raw_input('Pls input the size of the square:'))
a=[[]]*sz
for i in range(0,sz):
    if sz%2==0:
        if i%2==0:
            a[i]="# "*(sz/2)
        else:
            a[i]=" #"*(sz/2)
    else:
        if i%2==0:
            a[i]="# "*((sz-1)/2)+"#"
        else:    
            a[i]=" #"*((sz-1)/2)+" "
for j in a:
    print str(j)
