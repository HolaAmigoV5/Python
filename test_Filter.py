# -*- coding: utf-8 -*-
def is_palindrome(n):
    ss=str(n)
    if ss==str(n)[::-1]:
       return n

 # ²âÊÔ:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
