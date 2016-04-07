#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#list对象里面有多个tuple对象，dict对象表示为L={'Bob':75,'Adam':92,'Bart':66,'Lisa':88}
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    return t[0].lower()
L2=sorted(L,key=by_name)
print(L2)

def by_score(t):
    return t[1]
L3=sorted(L,key=by_score,reverse=True)
print(L3)