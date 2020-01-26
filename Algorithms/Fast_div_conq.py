#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:03:35 2019

@author: ElAwbery
"""

def inversions():
    integer_file = open('integers.txt', 'r')
    # Make an array of integers from the text file
    integers = []
    for line in integer_file.readlines():
        num = int(line.strip())
        integers.append(num)
        
    return integers

count = 0

def merge(left, right):
    '''righthalf and lefthalf are sorted lists'''
    global count
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
            count += len(left)-left_index
    
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
    

test1 = [1,3,5,2,4,6]
test2 = [1,5,3,2,4]
test3 = [5,4,3,2,1]
test4 = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ]
test5 = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 
         26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 
         31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ]

    
    
