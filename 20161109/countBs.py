#!/usr/bin/python
#-*- coding=utf-8 -*-

def countBs(s):
    ct=0
    for i in s:
        if i=='B':
            ct += 1
    print ct
