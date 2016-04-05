#! /usr/bin/python
# Filename : table_9x9.py
# Author : wby
# Date : 2016/04/5 18:22

print('\n9x9 Table\n')

for i in range(1, 10) :
    for j in range(1, i+1) :
        print(j, 'x', i, '=', j*i, '\t',)
    print('\n')

print ('\nDone!')
