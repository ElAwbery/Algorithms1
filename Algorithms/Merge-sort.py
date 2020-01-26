#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:36:21 2019

@author: ElAwbery
"""

# Brian Faure on youtube explains this well. 

def merge(left, right):
    '''righthalf and lefthalf are sorted lists'''
    result = []
    left_index, right_index = 0, 0
    # Walk along the lists with a pointer, don't mutate the lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
            
        else:
            result.append(right[right_index])
            right_index += 1
    
    if left_index == len(left):
        result.extend(right[right_index:])
    else:
        result.extend(left[left_index:])
    return result
        

def merge_sort(sequence):
    
    # base case is already sorted by definition:
    if len(sequence) <= 1:
        return sequence
    
    # keep breaking up the list until you get to base case lengths
    left = merge_sort(sequence[:len(sequence)//2])
    right = merge_sort(sequence[len(sequence)//2:])
    
    return merge(left, right)
        
        
print(merge_sort([0, 1, 3, 8, 2, 7, 7, 14, 0, 45, 3, 8, 9])) 
        
