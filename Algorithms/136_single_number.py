#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:20:27 2019

@author: ElAwbery
"""

class Solution(object):
        def singleNumber(self, nums):
            standard = 0
            for num in nums:
                standard = num ^ standard
                
            return standard
# using a bitwise operator, XOR: the logic is that for each number that repeats 
# its bit representation will reverse, cancelling it out. If the standard is 0
# then the final return will take account only of the 1 bit binaries in the 
# non bit duplicate
            
prob = Solution()
Input = [4,1,2,1,2]
Input2 = [2,2,1]

print(prob.singleNumber(Input))
print(prob.singleNumber(Input2))
