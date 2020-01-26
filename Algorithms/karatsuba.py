#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:18:23 2019

@author: Charlie
"""


# This works - the final line makes the difference. 
def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karatsuba(b,d)
        z1 = karatsuba((a+b),(c+d))
        z2 = karatsuba(a,c)
        
        
        result = (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)
        print(x, " * ", y, ": correct: ", x*y, " ours: " , result)

        return result








