#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:18:15 2019

@author: Charlie
"""

"""
Compute the number of comparisons (as in Problem 1), using the "median-of-three" 
pivot rule. [The primary motivation behind this rule is to do a little bit of 
extra work to get much better performance on input arrays that are nearly sorted 
or reverse sorted.] In more detail, you should choose the pivot as follows. 
Consider the first, middle, and final elements of the given array. (If the array 
has odd length it should be clear what the "middle" element is; for an array 
with even length 2k, use the kth element as the "middle" element. So for the 
array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) 
Identify which of these three elements is the median (i.e., the one whose value 
is in between the other two), and use this as your pivot. As discussed in the 
first and second parts of this programming assignment, be sure to implement 
Partition exactly as described in the video lectures (including exchanging the 
pivot element with the first element just before the main Partition subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), 
middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, 
you would use 4 as your pivot element.

SUBTLE POINT: A careful analysis would keep track of the comparisons made in 
identifying the median of the three candidate elements. You should NOT do this. 
That is, as in the previous two problems, you should simply add m-1m−1 to your 
running total of comparisons every time you recurse on a subarray with length m.
"""



comparison_count = 0
def quicksort_median(array):
    '''array is a list of integers
    returns the same list sorted from smallest to largest'''
    global comparison_count
    
    # Base case, array is already sorted
    if len(array) <= 1:
        return array
    # In simple version, pivot is always the first element of the array
    if len(array)%2 == 0:
        middle = (len(array)//2)-1
    else:
        middle = len(array)//2
   
    first_middle_last = [array[0], array[middle], array[len(array)-1]]
    
    first_middle_last.sort()
    median = first_middle_last[1]
    pivot_index = array.index(median)
    pivot = array[pivot_index]
    
    # swap pivot for first in array
    array[0], array[pivot_index] = array[pivot_index], array[0]
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

    # recursively sort the first part
    # recursively sort the second part
    return quicksort_median(array[0:i-1]) + [pivot] + quicksort_median(array[i:])



my_test = [4, 6, 2, 8, 45, 1, 98, 100, 3, 23]

final = [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]

Quicksort_file = open('QuickSort.txt', 'r')
final = []

for line in Quicksort_file.readlines()[0:10000]:
    num = int(line.strip())
    final.append(num)

quicksort_median(final)

print("comparisons", comparison_count)
print("final", final)
print("result_array", quicksort_median(final))

