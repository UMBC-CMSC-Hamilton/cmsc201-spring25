"""
Insertion Sort

    Quadratic Sort
    Preferred one in "industry" generally performs better than bubble or selection.

    What does insertion sort do?
        pull back sort, takes an element and it pulls it back into position

    [9, 8, 2, 7, 4, 6, 3, 5]
    i = 0 nothing you can do
    i = 1, can you pull 8 back? yes, by one element
    [8, 9, 2, 7, 4, 6, 3, 5]
    i = 2, you can pull this back 2 positions
    [2, 8, 9, 7, 4, 6, 3, 5]
    i = 3
    [2, 7, 8, 9, 4, 6, 3, 5]
    i = 4
    [2, 4, 7, 8, 9, 6, 3, 5]
    i = 5
    [2, 4, 6, 7, 8, 9, 3, 5]
    i = 6
    [2, 3, 4, 6, 7, 8, 9, 5]
    i = 7
    [2, 3, 4, 5, 6, 7, 8, 9]
"""
import random
import time


def insertion_sort(the_list):
    for start_index in range(1, len(the_list)):
        pull_back = start_index
        while pull_back > 0 and the_list[pull_back - 1] > the_list[pull_back]:
            temp = the_list[pull_back]
            the_list[pull_back] = the_list[pull_back - 1]
            the_list[pull_back - 1] = temp
            pull_back -= 1

    return the_list


"""
    We've seen three examples of sorts, Bubble, Selection and Insertion
        They all kind of have this n^2 / 2 number of steps for a list of size n, can we do better?
            Yes we can.  
    
    Merge Sort
    Idea:
        recursive sort
        divide the list in half 
        
        [10, 8, 2, 7, 3, 9, 4, 1]
        [10, 8, 2, 7]   [3, 9, 4, 1]
        [10, 8] [2, 7]  [3, 9] [4, 1]
        ([10] [8])  ([2] [7])  ([3] [9])  ([4] [1])
        ([8, 10]  [2, 7])  ([3, 9]   [1, 4])
                                |           |
        [2, 7, 8, 10]  [1, 3, 4, 9]
                  |                 |
         [1, 2, 3, 4, 7, 8, 9, 10]
                
"""


# some books call this merge  if |first| + |second| = n, this takes ~ n steps
def put_together(first, second):
    total_list = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            total_list.append(first[i])
            i += 1
        else:
            total_list.append(second[j])
            j += 1

    for x in range(i, len(first)):
        total_list.append(first[x])
    for y in range(j, len(second)):
        total_list.append(second[y])
    return total_list


print(put_together([1, 5, 7, 10], [2, 5, 6, 8]))


def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list

    half_way = len(the_list) // 2
    first_half = the_list[0: half_way]
    second_half = the_list[half_way: len(the_list)]

    # trust in recursion
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return put_together(first_half, second_half)


for size in [10, 100, 1000, 10000, 100000, 1000000]:
    new_list = [random.randint(0, 1000) for i in range(size)]
    start = time.process_time()
    merge_sort(new_list)
    print(f'Merge Sort sort took {time.process_time() - start} on {size} elements')


"""
Analysis:

    How many division steps does it take to divide a list of size n down to lists of size 1?
    How much work did we have to do in each step?
    
    100 => 50 => 25 => 12 => 6 => 3 => [1, 2] => 1
    128 => 64 => 32 => 16 => 8 => 4 => 2 => 1 [oh 2^7 = 128]
    256 => 128 [7 steps] => 1 [8 steps, 2^8]
    16 => 8 => 4 => 2 = > 1 [4 steps... 2^4 = 16]
    2^steps = list size = n
    2^s = n
    lg = log_2
    lg(2^s) = lg(n)
    s * lg(2) = lg(n)
    # steps = log base 2 of n
    
    Cost of each step is about n
    n * lg(n) steps, is this better than n^2? it seems to be... we'll look
        n lg(n) is way smaller than n^2, and therefore the run time of merge sort is better than 
            any quadratic sort.  
            
    QuickSort - fastest of the sorts, most of the time.  When it loses, it loses badly, it has a 
        fatal flaw.  
        
        picks the first element in the list and calls it the "pivot" - imagine a scale, not linear algebra

        Make two lists, a less list and a greater list
            Decide where equal elements go, into the greater list

    [8, 2, 9, 11, 5, 3, 1, 7, 8]
    pivot = 8 dont add the pivot to either list
    [2, 5, 3, 1, 7] [9, 11, 8]
    Quick sort these lists
    pivot = 2
    [1] [5, 3, 7]
    pivot = 5
    [3]  [7]
    [3, 5, 7]
    [1, 2, 3, 5, 7]
    
    Quicksort [9, 11, 8]
    pivot = 9
    [8] [11]
    [8, 9, 11]
    [1, 2, 3, 5, 7, 8, 8, 9, 11]
    
    
    ---------- badness of quick sort ----------
    [1, 2, 3, 4, 5, 6]
    pivot = 1
    [] [2, 3, 4, 5, 6]
    pivot = 2
    [] [3, 4, 5 ,6]
    pivot = 3
    [] [4, 5, 6]
    pivot = 4
    [] [5, 6]
    pivot = 5
    [] [6]
    
    [1, 10, 2, 9, 3, 8, 4, 7]
"""
