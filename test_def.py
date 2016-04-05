#! /usr/bin/python
# Filename : table_9x9.py
# Author : wby
# Date : 2016/04/5 18:22
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
       raise TypeError('is bad operand type')
    delta=b*b-4*a*c
    if a==0:
       if b==0:
          if c==0:
            print('无穷解')
          else:
            print('无解')
       else:
            print('只有一个解：',-c/b)
    elif delta>=0:
         x1=(-b+math.sqrt(delta))/(2*a)
         x2=(-b-math.sqrt(delta))/(2*a)
         return x1,x2
    else:
         delta<0
         print('解是共轭复根，我懒得算了')
         
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
