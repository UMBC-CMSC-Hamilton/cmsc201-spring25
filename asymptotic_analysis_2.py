"""

f(n) is O(g(n)) when there are constants C , N_0 so that
f(n) <= C g(n) for n >= N_0

f(n) is within a multiple of g(n), you get to pick the constant C
Sometimes early values like 0 especially can cause trouble, but we're looking
    at how algorithms run time changes when n is large, not small.

    N0 allows us to pick the starting point and after that all of the calculation is true
        before that its ok if theres exceptions.

3n^2 + 2n + 1 <= C * n^2
If you plug in any C = 1000
n = 0
0 + 0 + 1 <= 1000 * 0^2 = 0
Good news is that this happens with a dataset of size 0.  N0 = 5, push past the problem
    and the math works out.


f(n) is O(g(n)) when:
lim_{n \to infinity} f(n) / g(n) < infinity


lim_{n to infinity} sin(n) [you don't see these in CS most of the time]
    What algorithm does that? Nothing useful.


n^2 is O(n^3)

n^2 <= C n^3
divide by n^2

1 <= C * n
Pick C = 1, N_0 = 1 or 2


n^2 - 2n + 5 is O(n^3)

lim (n^2 - 2n + 5) / (n^3) = lim 1/n - 2/n^2 + 5/n^3 = 0 < infinity, so its true.


lg(n) is O(n)

lim lg(n)/n = lim (1/n) / 1 = 0 true.

lg(n) is O(sqrt(n))

lim lg(n) / sqrt(n) = lim (1/n) / (1/(2 sqrt(n)) = lim 2 n^{1/2} / n = lim 2/n^(1/2) = 0

Constants <= Logs <= roots <= O(n) <= O(n lg(n)) <= O(n^2) <= O(n^3) <= .. polynomials
Runnable stuff
<= O(2^n) <= O(3^n) ... <= O(n!) <= O(n^n) <= O(higher things, much worse)
                                                O((n!)^2) O((n^2)!) O(n^{n^2})
Really bad unrunnable stuff

O(n lg(n)) is the runtime for quicksort [in the good cases]
    merge sort
    heap sort
    any algorith where you have to sort first and then scan a list.


2^n <= n!
Proof:
    2 * 2 * 2 * 2 * ... * 2 <= 2 * 2 * 3 * 2 * ... * n
        n of them

    I stole a 2 out of the factorization of 4 to make this work, does that matter?

    1! = 1 < 2^1 = 2
    2! = 2 < 2^2 = 4
    3! = 6 < 2^3 = 8
    4! = 24 > 2^4 = 16 [something happened here]
    5! = 120 > 32
    6! = 720 > 64 etc... now its working and it works better and better
    7! = 5040 > 128 seems that n! is growing much faster

    2^n is O(n!)
    C = 1, N_0 = 4 [thats it starts working]


"""


def find_min(a_list):
    if not a_list:  # O(1) constant time
        return -1
    the_min = a_list[0]  # O(1) assignment, generally assignments, reads, writes are all constant
    for i in range(len(a_list)):  # O(n) - it scans through each index in the list
        if a_list[i] < the_min:  # constant time
            the_min = a_list[i]  # constant time
    return the_min


# O(2n + 3) = O(n)
# 2n + 3 <= 5n , n > 0


def is_prime(n):
    if n == 0 or n == 1:
        return False
    # n = a * b then either a or b are less than or equal to the square root of n
    # proof: if not, a > sqrt(n) b > sqrt(n), oops [contradiction]
    # 25 = 5 * 5, 12 = 2 * 6, 3 * 4, 51 = 3 * 17
    for x in range(2, int(n ** (1 / 2)) + 1):
        if n % x == 0:
            return False

    return True


# algorithm runs in O(sqrt(n)) time.


"""
Binary Search

Linear Search O(n) time, called linear
"""


def linear_search(a_list, element):  # O(n) algorithm, nothing special
    for x in a_list:  # takes about n steps [maximum] to find the element
        if x == element:
            return True
    return False


"""
Binary Search = what if the list were sorted?  

[2, 6, 8, 10, 14, 21, 77, 93]
looking for 6
len(list) //2 = 8 // 2 = 4 = index we check
list[4] = 14, we know that IF 6 in the list then it's on the left side.  

len(sublist) = 4 // 2 = 2
list[2] = 8, still too big, go left again

[2, 6]
len(list) = 2
2//2 = 1, look at index 1
list[1] == 6, we return True

For instance if the list starts out at a size of 100
100 => 50 => 25 => 12 => 6 => 3 => 1 => 0 [elements]

Somewhere between 6 and 7 steps.  
128 => 64 => 32 => 16 => 8 => 4 => 2 => 1 [7 steps]

256 => 128 => [7 steps] == [8 steps]

n = 2^p, solving for p
lg(n) = lg(2^p) = p
lg(n) = log base 2 rather than ln, log, whatever

log_b(x) = log_a(x) / log_a(b)

lg(n) = ln(n) / ln(2)
"""
import random


# search a_list for element
def binary_search(a_list, element):  # O(lg(n)) algorithm, faster even than the prime checker
    if not a_list:
        print('Empty list element not found')
        return False
    midpoint = len(a_list) // 2

    print(a_list, a_list[midpoint])

    if element == a_list[midpoint]:
        return True
    elif element < a_list[midpoint]:
        return binary_search(a_list[0: midpoint], element)
    else:
        return binary_search(a_list[midpoint + 1:], element)


my_list = [random.randint(0, 100) for _ in range(20)]
my_list.sort()
print(my_list)
x = int(input('What do you want to search for? '))
print(binary_search(my_list, x))