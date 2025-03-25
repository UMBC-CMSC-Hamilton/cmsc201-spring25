"""
    Functions are a method to isolate code from the rest of your program

    allow you to have a single piece of functionality that does the same task over and over
    allows you to send an arguments/parameter(s) into the function
    The function can take that data and work on it and produce different output.

    They also provide 'scope' meaning there is a local scope and global scope

    global scope - all variables declared outside of functions
        they have a lifetime of the the entire program
        they're accessible anywhere so you never really know if another
            function has changed or not
    local variables / local scope - they exist inside of a function
        their lifetime is the length of the function call
        they're not accessible from outside of the function or other functions

    return allows a value to be sent back from the function to the global scope
        or to another function
"""


def count_vowels(sentence):
    VOWELS = ['a', 'e', 'o', 'i', 'u', 'y']
    count = 0
    for letter in sentence:
        if letter.lower() in VOWELS:
            count += 1
    return count


# return takes the value not the name
x = count_vowels('hello there i am a sentence')
print(x)

# print(count), cant print count because it no longer exists, it was in local scope

count_vowels('asdfwqroiewlkjfdslkjfdsoiuewlkjfdslkjfsoi')
# if you dont save the returned value from a function, that value is lost

# return and print are different.
# return just gives you a value, returns it to the global scope so it can be saved
# into a variable or printed
# it doesn't print anything out.

"""
You kind of know this already

"""


# the_string = input("tell me something")

#                   parameters
def check_for_subset(a_list, b_list):
    """
    Checks if all of the elements of a_list are in b_list.

    :param a_list:
    :param b_list:
    :return: True or False
    """
    sub_check = True
    for x in a_list:
        if x not in b_list:
            sub_check = False

    return sub_check


#                           these are arguments = the data you are actually sending in
print(check_for_subset([1, 2, 3], [2, 3, 4, 5]))
print(check_for_subset([1, 2, 3], [2, 3, 4, 5, 1, 2, 3]))


def is_substring(a_string, b_string):
    """
        a_string in b_string

    :param a_string:
    :param b_string:
    :return:
        012 0123456789 10 11 12 13 14
        abc tqaxrbabfa b  c  d  e  f

    """
    # detected = True  # just makes sure we dont go outside of the b_string
    for start in range(len(b_string) - len(a_string) + 1):
        detected = True
        for i in range(len(a_string)):
            if a_string[i] != b_string[start + i]:
                detected = False
        if detected:
            return True

    return True


print(is_substring('abc', 'aslkjfdslkjfdslkjabclkjfdslkjabc'))
print(is_substring('xy', 'xabyabz'))
input('>> ')
print(is_substring('asfdasfdasfdasfdsadf', 'abc'))

'''
What is an edge case?
    Its a case that has to be handled separately, or behaves differently
        to most of the other cases.  

What is a corner case?
    An even more rare case, multiple edge cases put together. 
'''


def is_prime(n):
    if n < 2:  # this if statement isolates the edge cases
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


"""
    base data types:
        int bool str float are called immutable
    mutable data types
        dict, list, set[dont learn it, like a dictionary]
        +others, can be changed
"""


def add_one(x):
    x = x + 1
    print('inside', x)


def concat_an_apple(my_string):
    my_string += 'apple'
    print(my_string)
    return my_string


def append_one(the_list):
    the_list.append('a')
    print('inner', the_list)


# because integers are immutable, they are "passed by value", copy not renamed
# the local variable is a copy of the global variable, not the value itself
r = 7
add_one(r)
print('outside', r)

# lists are mutable, so they get "passed by reference"
# two variables are references of each other when they refer to the same exact piece
# of data in memory, it's a renaming not a copy
my_list = ['r', 't', 'p', 'q', 'x']
append_one(my_list)
print('outer', my_list)

# strings are IMMUTABLE so they pass by value (a copy is made)
outer_string = 'hello '
outer_string = concat_an_apple(outer_string)
print('outer: ', outer_string)

"""
How do you return multiple things?

return x, y [this is a tuple an immutable list]
return (x, y) # this is what it does automatically to the case above
return [x, y] also works
"""


def get_user_and_password():
    un = input('What is your username? ')
    pw = input('Password: ')
    return [un, pw]


user_and_password_pair = get_user_and_password()
print(user_and_password_pair)
print(type(user_and_password_pair))
print(user_and_password_pair[0])
user_and_password_pair[1] = 'robotsattack'


"""
    Important concepts:
        Mutability vs pass by reference and pass by value
            Immutable <-> Pass by Value [makes a copy]
            Mutable <-> Pass by reference [both variables refer to the same data]
                if you modify one you modify the other one
        Local vs Global Scope     
"""

a_list = [1, 2, 3]
b_list = a_list # what is this? it has to be a reference because if it was a copy this wouldnt modify a_list
b_list[1] = 44
print(a_list)

# how do you make a copy of a list?
copy_list = list(a_list)
