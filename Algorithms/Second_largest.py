#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:07:02 2019

@author: ElAwbery
"""


def same_index_element(array):
    '''binary search to find whether there is an element equal to its index number in the list'''
    if array == []:
        return False
    
    midpoint = len(array)//2
    
    if array[midpoint] == midpoint:
        return "array index number " + str(midpoint) + " is integer " + str(array[midpoint])
    
    # The match can only lie on the r side of midpoint
    elif array[midpoint] < midpoint:
        return(same_index_element(array[midpoint:]))
    # The match can only lie on the l side of midpoint
    else:
        return(same_index_element(array[:midpoint]))
        

test = [1, 4, 8, 9]   
test2 = [0]
test3 = [0, 4, 7, 10]
test4 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
test5 = [0, 1, 2, 3, 3, 4, 4, 7, 12, 15, 18, 18, 22, 55]
