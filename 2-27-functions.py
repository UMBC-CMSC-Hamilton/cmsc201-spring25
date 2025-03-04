"""
    Control Flow:
        Sequential - execute one line after another
        Conditional - execute only if a condition is met, otherwise it jumps over the
            condition (if/elif/else : match/case)
        Iterative - executes a block of code [a set of lines] multiple times
            for, while
        Functional - Jump to the function's code, you execute it, and then you return
            to the original place where the function was called

    Why do that?
        Certain functions we already know and use
            print, input, strip, split, join, len, etc...
            Do you want to rewrite split every time you have to use it? no

"""


#               parameter = data that will be sent into the function
#               temporary name that we call that piece of data inside the function
#               local variable, a variable that exists inside of the function
def count_evens(a_list):
    num_evens = 0
    for x in a_list:
        if x % 2 == 0:
            num_evens += 1
    # return is a way to give data back to the place where the function was called
    return num_evens


def another_function():
    x = 3
    print('hi i am a function')
    # secretly returns None at the end


"""
What does this function need to know? 
    My function needs to know the number we're about to test, i'll call it n
What does my function need to tell me?
    Whether the number is prime or not, that's what you're going to return
"""


def is_prime(n):
    # because the return is inside of the if statement, it'll only return False when n <= 1
    # otherwise the function keeps going
    if n <= 1:
        return False

    # 0 gives ZeroDivisionError, 1 is weird, start at 2
    # boolean flag - boolean variable that tracks something in your program
    number_is_prime = True
    # because range goes up to n - 1 but not equal to n, we're ok there
    for factor in range(2, n):
        # you must have this if statement here
        if n % factor == 0:
            # this should only happen once, will happen when we find the first factor
            number_is_prime = False
            # return False # also acceptable

    return number_is_prime


"""
    What does split need to know?
        needs to know the string we want to split up
    what does it give back to us?
        a list of strings ==> return
"""


def split(a_string):
    """
        Splits a string on whitespace

    :param a_string: string parameter to be split
    :return: a list of strings
    """
    # a_string += " " this will also work, it's a bit more weird
    split_list = []

    whitespace = [' ', '\t', '\n', '\r']
    current_string = ''
    for c in a_string:
        if c in whitespace and current_string:  # 'asdf    asdf'
            split_list.append(current_string)
            current_string = ''
        elif c not in whitespace:
            current_string += c

    # "abcd efgh jikl" current_string = 'jikl' but there's no character after it
    if current_string:
        split_list.append(current_string)

    return split_list  # go back to global scope


def display_board(the_board):
    """
    This function prints out the tic-tac-toe board

    :param the_board: this is a 2d-tic-tac-toe board
    :return: None
    """
    for i in range(len(the_board)):
        print(' | '.join(the_board[i]))
        if i != len(the_board) - 1:
            print('-' * 9)


"""
    Think of another example? 
        
"""


def main_menu():
    command = input('>> ')
    while command != 'quit':
        if command == 'play':
            print('You are going to play the game')
        elif command == 'load':
            print('You are about to load a file')
        elif command == 'save':
            print('Saving game')
        elif command == 'quit':
            print('Goodbye')
        command = input('>> ')

"""
    Functions can have any number of parameters
        the parameters can be any type
"""
def distance(x_1: float, y_1: float, x_2: float, y_2: float):
    d = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
    d **= 0.5
    return d


def create_some_vars():
    x = 4
    y = 17
    print(f'x: {x}, y: {y}')


if __name__ == "__main__":
    main_menu()

"""
    Global Scope:
        outside of all functions
        the variable names are accessible anywhere
        variables live as long as the program lives
    Local Scope:
        Variables inside of functions
        they live only as long as the function is being called
            every time you call a function, it's a fresh start
        local variables are only accessible inside the function where they exist
            create a variable called count inside of a function
        When you leave the function all of the variable names/variables are destroyed
            UNLESS you return it, you're only returning the value
"""

"""
    Functions allow us to have a single place where that functionality happens
        if theres a bug you dont have to look everywhere in your code, just 
            at that one function until you fix it.  
"""

my_list = [1, 5, 7, 3, 4, 2, 10, 3, 6, 8, 2, 4, 5, 6, 7]
print(count_evens(my_list))
another_list = [2, 3, 4, 5, 6, 7, 8]
the_count = count_evens(another_list)

# this shouldn't to be too foreign to you because input does exactly that
my_name = input('tell me a name: ')
# my_name is returned by input

another_function()
var = another_function()
print(var)

x = print('hello everyone')
print(x)

is_prime(15)

my_string = 'asdf asdf sadf dsaf asf'
# my_string.split() standard function we're not using that
print(split(my_string))

game_board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
display_board(game_board)

create_some_vars()
# print(x, y)

a_string = 'once upon a time there was a little program'
# remember that if you dont save a returned value into a variable, it's lost.
result = split(a_string)
print(result)


print(distance(3.2, 2.1, 5.9, 8.7))
# print(distance('hi', 'bye', 'no', 'yes'))
