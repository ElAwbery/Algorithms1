"""
Created on Thu Dec 19 14:36:44 2019

@author: ElAwbery
"""

"""
This is the second version of Quicksort, taking the final element of the 
input array as the pivot. 

Compute the number of comparisons (as in Problem 1), always using the final 
element of the given array as the pivot element. Again, be sure to implement 
the Partition subroutine exactly as it is described in the video lectures.

Recall from the lectures that, just before the main Partition subroutine, 
you should exchange the pivot element (i.e., the last element) 
with the first element.
"""

comparison_count = 0
def quicksort_pivot_end(array):
    '''array is a list of integers
    returns the same list sorted from smallest to largest'''
    global comparison_count
    
    # Base case, array is already sorted
    if len(array) <= 1:
        return array
    # In simple version, pivot is always the first element of the array
    pivot = array[len(array)-1]
    # swap pivot for first in array
    array[0], array[len(array)-1] = array[len(array)-1], array[0]
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
    return quicksort_pivot_end(array[0:i-1]) + [pivot] + quicksort_pivot_end(array[i:])



my_test = [4, 6, 2, 8, 45, 1, 98, 100, 3, 23]

final = [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]

Quicksort_file = open('QuickSort.txt', 'r')
final = []

for line in Quicksort_file.readlines()[0:10000]:
    num = int(line.strip())
    final.append(num)
quicksort_pivot_end(final)

print("comparisons", comparison_count)

print("final", final)
print("result_array", quicksort_pivot_end(final))

