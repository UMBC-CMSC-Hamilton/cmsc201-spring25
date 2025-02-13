"""
    Extend homework 2 until monday.
    Still put out homework 3 on friday.

    For loops and lists, they work together in python for the most part

"""

"""
List out the numbers between 1 and 10
    range gives you every integer between 0 and the upper limit [not inclusive]
    
    How do we fix this?
"""
if False:
    for index in range(11):
        if index != 0:
            print(index)

    # start at i = 1 and go up to but not including i = 11 [last one is i = 10]
    for i in range(1, 11):
        print(i)


    # next level is adding up numbers 1 + 2 + 3 + 4  + 5 + ... + n

    n = int(input('What number do you want to add up to? '))

    total = 0
    # now with the n + 1 it will include the n as our last number
    for i in range(1, n + 1):
        # I need a variable that counts up the total
        # do I need to declare it inside the loop or outside the loop?
        # total = total + i
        total += i  # short hand notation for the above line

    print('Total = ', total)


    """
    What is factorial?
    n! = 1 * 2 * 3 * 4 * 5 * ... * (n- 1) * n
    2! = 1 * 2
    3! = 1 * 2  * 3
    Define:
    0! = 1
    """

    n = int(input('What number do you want to calculate factorial? '))

    total = 1
    # now with the n + 1 it will include the n as our last number
    for i in range(1, n + 1):
        total *= i

    print('Factorial = ', total)

# python handles very large integers, but beware that multiplication of super-large numbers is slow

"""
    Lists in python are a way to store data in a sequence
    
"""
# indexing into a list always counts offset not element
#         1st  2nd  3rd
a_list = [7,   3,   9,   1, 4, 5, 8, 2]
#  index  0    1    2    3  4  5  6  7

# to access elements from a list you need their index
print(a_list[3], a_list[0], a_list[7], a_list[5])

# to modify an element inside of a list you do the same thing

a_list[4] = 21
print(a_list)
# print(a_list[52])

index = int(input('Which index should I print? '))
if 0 <= index < len(a_list):  # notice that the upper end has to be < [strict]
    print(a_list[index])
else:
    print(f'{index} was out of range')

# how do you add a new element into a list?
#   append

b_list = []
b_list.append(5)
b_list.append(17)
b_list.append('hello')
b_list.append(True)
b_list.append(4.56)
print(b_list)


word_list = ['voluptuous', 'epic', 'defenestration', 'treaty', 'nonary', 'voluntary']

# range eats an integer not a list
# len can take a list give a number back, so thats what we need to do first
for index in range(len(word_list)):
    print(word_list[index])
    # as it turns out you can treat strings as a sort of list
    if word_list[index][0].lower() == 'v':
        print(f'{word_list[index]} is a v word')

num_vowels = 0
num_consonants = 0
a_string = 'defenestration'
for letter in a_string:

    # doesn't work because of order of operations
    # if letter == 'a' or 'e' or 'i' or 'u' or 'y':
    #     print(letter, 'is a vowel')

    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        print(letter, 'is a vowel')

    if letter == 'a' or letter == 'e' or letter == 'i' or \
            letter == 'o' or letter == 'u' or letter == 'y':
        num_vowels += 1
    else:
        num_consonants += 1

print('v: ', num_vowels, 'c: ', num_consonants)

if 'e':
    print('E is true')

if '':
    print('empty is true')
else:
    print('Empty is false')

if '     ':
    print('spaces are true')

"""
For strings:
    non-empty => True
    empty => False

For Integers and Floats:
    0 => False
    anything else => True
For Lists:
    Empty => False
    anything else => True
"""

if not a_list:
    pass  # this returns true if the list is empty

"""
Getting back to for loops
"""

c_list = [1, 4, 6, 7, 3, 7, 3, 8, 9]
"""
add up only the even numbers
3 = 2k      even
3 = 2k + 1  odd

0 = 2k pick k = 0, even
"""
total_evens = 0
for i in range(len(c_list)):
    if c_list[i] % 2 == 0:  # this divides evenly by 2
        total_evens += c_list[i]
    # c_list[i] = 87, if you need to modify the list you must use a for-i loop

other_total_evens = 0
for number in c_list:
    if number % 2 == 0:
        other_total_evens += number
    number = 7 # this doesn't actually change the list, only the temporary values

print(c_list)
print(total_evens, other_total_evens)
"""
    Downside is that you can't know which index it's coming from anymore
    so you're not allowed to modify elements in the list
"""

num_vowels = 0
for word in word_list:
    for letter in word:
        if letter == 'a' or letter == 'e' or letter == 'i' or \
                letter == 'o' or letter == 'u' or letter == 'y':
            num_vowels += 1
print(f'The list had {num_vowels} vowels')


size = 10

for y in range(size):
    for x in range(size):
        if x == y:
            print('*', end="")
        elif x == size - 1 - y:
            print('*', end="")
        else:
            print(' ', end="")
    print()
