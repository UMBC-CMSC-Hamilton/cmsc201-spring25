import sys

sys.setrecursionlimit(5000)

""""
What is Recursion?

    Where a function calls itself.

    most basic examples of recursion
        these are not 'useful' but that's not the point.  The point is to understand
        what they're doing.

    What if we want to add up the numbers from 1 to n
        Smart Way: use a for loop
            total = 0
            for i in range(n + 1):
                total += i
            return total
        Other Way:
            In order to add up the numbers from 1 to n, you must add up the numbers
                from 1 + ... + (n - 1) then you add n on the end.

"""


def add_up(n):
    if n == 0:
        return 0

    return add_up(n - 1) + n


"""
add_up(2) + 3
add_up(2) = add_up(1) + 2
add_up(1) = add_up(0) + 1 stop here
add_up(0) = add_up(-1) + 0 or here
add_up(-1) = add_up(-2) + -1 not here
    not all the others 
"""

print(add_up(3))
print(add_up(100))
print(add_up(25))

"""
factorials [the same problem but now with multiplication]

for loop definition
n! = 1 * 2 * 3 * 4 * 5 * ... * (n - 1) * n
0! = 1 [definition]

recursive definition:
n! = (n - 1)! * n
factorial(n) = factorial(n - 1) * n

0! = 1 [base case]

"""


def factorial(n):
    if n <= 0:
        return 1
    fnm1 = factorial(n - 1)
    print(n, fnm1)
    return fnm1 * n


print(factorial(10))
print(factorial(4))
print(factorial(5))
print(factorial(100))

"""
Branching Recursion
    one recursion calls multiple subrecursions
    
Fibonacci numbers.  
a list of numbers and you add the previous two to get the next one
[fib == start with 1, 1]
0 1 2 3 4 5 ...
1 1 2 3 5 8 13 21 34 55 89 144 233 so on

fib(n) = fib(n - 1) + fib(n - 2)
What is our base case?


        fib(5) ----------------------------
          |                               |
        fib(4)                          fib(3)
          |-------------                  |------------
        fib(3)       fib(2)             fib(2)      fib(1)
          |--------      |--------         | base case = stop
        fib(2)  fib(1)   fib(1) fib(0)  fib(1)  fib(0)
          |-------
        fib(1)  fib(0)
        
        
        fib(6)
          |--------------------------------------------
        fib(5)                                        |
          | the entire previous digram              fib(4) = the fib(4) part of the diagram
"""


def fib(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0

    return fib(n - 1) + fib(n - 2)


for i in range(20):
    print(fib(i))


n = int(input('What fib do you want to calculate without recursion? '))
prev = 1
prev_prev = 1

for i in range(2, n):
    current = prev + prev_prev
    prev_prev = prev
    prev = current

print(current)
