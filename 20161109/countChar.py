#!/usr/bin/python
#-*- coding=utf-8 -*-

def countChar(s,sf):
    ct=0
    for i in s:
        if i==sf:
            ct += 1
    print ct
