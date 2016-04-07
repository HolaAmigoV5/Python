# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):   
     inx=len(s)- s.index('.')-1
     s=s.replace('.','')
     def fn(x,y):
         return x*10+y
     def char2num(s):
         return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
     def displa(i):
         return 10**i
     #return (reduce(fn,map(char2num,s)))/(displa(inx))
     return (reduce(fn,map(char2num,s)))/(pow(10,inx))
    
print('str2float(\'123.456\') =', str2float('123.456'))