#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#����һ��������
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

#����һ��ɸѡ����
def _not_divisible(n):
    return lambda x:x%n>0

#����һ�������������Ϸ�����һ������
def primes():
    yield 2
    it=_odd_iter() #��ʼ������
    while True:
        n=next(it) #�������еĵ�һ����
        yield n
        it=filter(_not_divisible(n),it) #����������

for n in primes():
    if n<1000:
        print(n)
    else:
        break