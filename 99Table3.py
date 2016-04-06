#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L=[str(j)+'×'+str(i)+'='+str(i*j) for i in range(1,10) for j in range(1,i+1)]
print(L[::1])
