#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open ('./111.txt','r') as f:
    #print(f.read())
    for line in f.readlines():
        print(line.strip())