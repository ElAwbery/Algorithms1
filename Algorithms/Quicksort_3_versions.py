#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:29:51 2019

@author: ElAwbery
"""

"""
Your task is to compute the total number of comparisons used to sort the given 
input file by QuickSort. As you know, the number of comparisons depends on which 
elements are chosen as pivots, so we'll ask you to explore three different 
pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive 
call on a subarray of length m, you should simply add m-1 to your running total 
of comparisons. (This is because the pivot element is compared to each of the 
other m-1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, 
and different implementations can give you differing numbers of comparisons. 
For this problem, you should implement the Partition subroutine exactly as it 
is described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:
For the first part of the programming assignment, you should always use the 
first element of the array as the pivot element.

1: 162085
2: 164123
3: 138382



"""

comparison_count = 0
def simple_quicksort(array):
    '''array is a list of integers
    returns the same list sorted from smallest to largest'''
    global comparison_count
    
    # Base case, array is already sorted
    if len(array) <= 1:
        return array
    # In simple version, pivot is always the first element of the array
    pivot = array[0]
    # partition the input array around pivot using in-place implementation
    # so that memory use is minimalized
    i = 1  # the boundary in the seen elements between < pivot and > pivot
    j = 1  # the boundary between the elements looked at and those not yet seen
    for index in range(1, len(array)):
        
        if array[index] < pivot:
            j += 1
            array[index], array[i] = array[i], array[index]
            i += 1
        else:
            j += 1
            
    comparison_count += (len(array)-1)

    # swap the pivot element to its rightful place
    array[0], array[i-1] = array[i-1], array[0]
    print("comparisons", comparison_count)

    # recursively sort the first part
    # recursively sort the second part
    return simple_quicksort(array[0:i-1]) + [pivot] + simple_quicksort(array[i:])



Quicksort_file = open('QuickSort.txt', 'r')
final = []

for line in Quicksort_file.readlines()[0:10]:
    num = int(line.strip())
    final.append(num)
    
simple_quicksort(final)

