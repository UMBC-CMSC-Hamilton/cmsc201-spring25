"""
1) B
2) D
3) B
4) B
5) C
6) C
7) B
8) D
9) C
10) B
11) B
12) D
13) C
14) A
15) A


16. Write a boolean expression which is True if and only if “happy” is a substring
of emotions and ‘recursion’ is in the list concepts but ‘polymorphism’
is not in that list.

17. Write a boolean expression which is True if and only if the last_train variable is equal
to ’San Fernando’, an integer track is set to an odd number and the time is “11:59”.
18. Write a boolean expression which is True if and only if the dictionary textttpeople has ‘Eric’
and ‘Claire’ or has at least 100 people (keys).
"""
# this is just an example to make sure the code doesn't fail here.
emotions = 'happy sad'
concepts = []
# this is all you need
'happy' in emotions and 'recursion' in concepts and 'polymorphism' not in concepts

time = "03:28"
last_train = 'San Fernando'
track = 7
track % 2 == 1 and last_train == 'San Fernando' and time == "11:59"

people = {}
('Eric' in people and 'Claire' in people) or len(people) > 100
# this one below is not the right one, notice a different set of ()
'Eric' in people and ('Claire' in people or len(people) > 100)

"""
20. Explain how local variables differ from global variables. Include at least two differences. You
may want to talk about scope.

    Lifetime = Local variables exist inside of a function in local scope, when the function ends,
        those variables [variable names] are lost.
    Accessibility = Local variables are accessible inside of the function but not by other
        functions or in the global scope
    Lifetime - Global variables live as long as the program does.  
    Accessibility - They are always accessible from either global or local scopes.  

21. Explain why pass-by-value and pass-by-reference are different. Explain how Python deter-
mines how to pass variables in each case.

    Python determines which type of passing by the type of variable, if it's immutable [int bool float, string, NoneType, others]
        then it passes by value, else its mutable and passes by reference [list, dict, classes].
    Pass by value makes a copy of the value of the variable and so the original is not modified if the local variable is.
    Pass by reference creates an alias of the new local name, but the variable is actually the same, so modifying it
        does change the list or dictionary, or class.  
    
22. Write an example of a recursion without a base case and show that it will recursive infinitely.
Explain why the base case is necessary.

    def fib(n):
        return fib(n - 1) + fib(n - 2)
    
    fib(2) = fib(1) + fib(0)
    fib(1) = fib(0) + fib(-1)
    fib(0) = fib(-1) + fib(-2)
    fib(-1) = fib(-2) + fib(-3)
    fib(-2) = fib(-3) + fib(-4)
    so on forever... 
    
    
    def countdown(n):
        return countdown(n - 1)

searching for 15
15 found
searching for 22
22 not found
searching for 50
50 found
searching for 24
24 not found


"""


def square(x):
    print(x, x ** 2)
    return x ** 2


def difference_quotient(x, y, z):
    print(x, y, z)
    return (x - y) / z


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return n


def do_calculations():
    print(difference_quotient(factorial(4), factorial(3), 2))
    print(difference_quotient(square(6), square(3), 3))


if __name__ == '__main__':
    do_calculations()

"""
print(difference_quotient(factorial(4), factorial(3), 2))
factorial(4) = 4* 3* 2 * 1 = 24
factorial(3) = 3 * 2 + 1 = 6
print(difference_quotient(square(6), square(3), 3))


24 6 2
9.0 [ .0 is because of the / rather than //]
6 36
3 9
36 9 3
9.0
"""


def double_list(the_list):
    i = 0
    the_length = len(the_list)
    while i < the_length:
        the_list.append(the_list[i])
        i += 1
    return the_list


my_list = [1, 2, 3]
double_list(my_list)
print(my_list)

"""
my_list = [1, 2, 3, 1, 2, 3]
i = 3 then the original list length was 3 and the while loop says while i < original length
this is also a mutability question.  
Answer:
[1, 2, 3, 1, 2 ,3]
If we made a copy then the answer would be 
[1, 2, 3]
"""

big_string = 'random.nonsense'
print(big_string[5:12])
print(big_string[0:8])
print('the output is', big_string[17:])

# m.nonse
# random.n
# [empty] - exception from the normal way of python, no IndexError, or any other kind of issue.
# understand that slices are the exception to IndexErrors

""""""


def how_far(num):
    if num % 3 == 0:
        return 1
    else:
        return how_far(num // 4) + 1


print(how_far(37), 'steps')
"""
hf(37) = hf(9) + 1 = 2
hf(9) = 1

2 steps

"""

value = 4
while value < 50:
    value *= 2
    value -= 3
    print(value)

"""
5
7
11
19
35
67
"""

my_list = []
row_list = []
for i in range(4):
    row_list.append(i + 1)  # row_list = [1, 2, 3, 4]

my_list = [row_list, row_list, row_list]
my_list[2][2] = 7  # row_list = [1, 2, 7, 4]
for row in my_list:
    print(row)
# [1, 2, 7, 4]
# [1, 2, 7, 4]
# [1, 2, 7, 4]
