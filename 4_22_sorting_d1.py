"""
https://visualgo.net/en/sorting

Quadratic Sorts

    n^2 steps to run on a list of size n


BubbleSort - adjacent elements and swap them if needed

[6, 3, 9, 1, 4, 7]
[3, 6, 1, 4, 7, 9]
[3, 1, 4, 6, 7, 9]
[1, 3, 4, 6, 7, 9] - scan for it i'll show you how that works.

[5, 4, 3, 2, 1]
[4, 3, 2, 1, 5] - every swap happens (4 swaps)
[3, 2, 1, 4, 5] - 3 swaps
[2, 1, 3, 4, 5] - 2 swaps
[1, 2, 3, 4, 5] - 1 swap

reverse sorted list of size 5 ==> 1 + 2 + 3 + 4 swaps
reverse sorted list of size n ==> 1 + 2 + 3 + ... + (n - 1) swaps we'll talk about the formula in a minute

# swaps is about
    1 + 2 + 3 + ... + n

    1 + 2 + 3 + 4 + 5 + 6  =
    = 7 * 6 / 2 = 42/2 = 21
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
    9 * 8 / 2 = 36

    1 + 2 + 3 + 4 + 5 + 6 + 7 = 8 * 7 / 2 = 28

    1 + 2 + 3 + ... + n = n * (n + 1) / 2
    Arithmetic Formula, Gauss Sum.

    Notice that n( n + 1) / 2 = --> n^2 <-- / 2 + n / 2
"""
import random
import time


def bubble_sort(the_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(the_list) - 1):
            if the_list[i] > the_list[i + 1]:
                swapped = True
                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp

    return the_list


bigger_list = [random.randint(0, 100) for _ in range(20)]
print(bigger_list)
bubble_sort(bigger_list)
print(bigger_list)

my_list = [1, 8, 2, 5, 2, 5, 7, 3, 5]
bubble_sort(my_list)
print(my_list)


"""
    find the min put it in slot 0
    find the next element put it in slot 1
    ...
    at the end and you're done

    n checks on the first loop
    n - 1 checks on the next
    n - 2 checks
    n - 3
    ...
    1
    n ( n + 1 ) / 2 steps just like bubble sort.  
"""
def selection_sort(the_list):
    for i in range(len(the_list)):
        min_index = i
        for j in range(i, len(the_list)):  # start at i to ignore previous work
            if the_list[j] < the_list[min_index]:
                min_index = j
        temp = the_list[i]
        the_list[i] = the_list[min_index]
        the_list[min_index] = temp
    return the_list



def insertion_sort(the_list):

    for start_index in range(1, len(the_list)):
        pull_back = start_index
        while pull_back > 0 and the_list[pull_back - 1] > the_list[pull_back]:
            temp = the_list[pull_back]
            the_list[pull_back] = the_list[pull_back - 1]
            the_list[pull_back - 1] = temp
            pull_back -= 1

    return the_list


check_sel = [random.randint(0, 100) for _ in range(20)]
selection_sort(check_sel)
print(check_sel)
new_list = [random.randint(0, 1000) for i in range(10000)]

start = time.process_time()
bubble_sort(list(new_list))
print(f'Bubble sort took {time.process_time() - start}')

start = time.process_time()
selection_sort(list(new_list))
print(f'Selection sort took {time.process_time() - start}')


for size in [10, 100, 1000, 10000, 100000]:
    new_list = [random.randint(0, 1000) for i in range(size)]
    start = time.process_time()
    bubble_sort(list(new_list))
    print(f'Insertion sort took {time.process_time() - start} on {size} elements')
