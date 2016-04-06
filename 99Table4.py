#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def NineTable(row):
	L=[str(i)+'×'+str(row)+'='+str(i*row) for i in range(1,row+1)]
	yield L

n=1
while n<10:  
    for t in NineTable(n):
        print (t)
        n=n+1