"""
    Strings are collections of characters
        !@#$%^&*()<>:{}
        1234567890
        asdf
        ASDF

        escape characters:
            \n = newline
            \t = tab = these can be used in many different ways
            \\ = single backslash
            \r = carriage return
            \" = double quote
            \' = single quote

    you can treat strings as lists, but you can't modify them

    strings are called "immutable" they cannot be changed
    if you want to modify a string you actually create a new string

    lists are mutable so can be modified
"""

my_string = 'hello there'
# my_string[4] = 'b'
# convert it into a list first
my_characters = list(my_string)
print(my_characters)
my_characters[4] = 'b'
print(my_characters)
"""
    How do we convert this list back into a string?
        we use the join function
    takes a separator and a list of strings
        joins them together with the separator
   
   to modify a string;
        string -> list(the_string) [converts to a list]
                            |
                            v
        string  <- modify it and convert it back with join     

    separator.join(the_list)
"""

print(my_string)

my_list = ['a', 'b', 'c', 'd']
print('-'.join(my_list))
print(':X:'.join(my_list))
print('\t'.join(my_list))
print(''.join(my_characters))

my_numbers = [1, 2, 3, 4, 5]
my_cast = []
for i in range(len(my_numbers)):
    my_cast.append(str(my_numbers[i]))
# am i going to use the my_numbers list again? if no, then just cast,
#       otherwise make a new list
print('.'.join(my_cast))


"""
split() is the opposite of join
 choose a separator (or general whitespace if you don't) you can separate strings 
 based on that separator
"""

the_string = input('Tell me a string: ')
while the_string != 'quit':
    print(the_string.split())
    the_string = input('Tell me a string: ')

phone_number = '805-445-8965'
other_number = '443.566.2321'

print(phone_number.split('-'))
print(other_number.split('.'))

split_nonsense = 'abcabbacababacacab'.split('ab')
print(split_nonsense)
print('ab'.join(split_nonsense))

command = input('Enter a command: ')
print(command.split())
split_command = command.split()
if split_command[0] == 'insert':
    value = int(split_command[1])


"""
    strip() = removes whitespace from the beginning and end of the string
        NOT FROM THE MIDDLE
"""

the_string = input('Tell me a string: ')
while the_string != 'quit':
    print(the_string.strip())
    the_string = input('Tell me a string: ')

#
s = ''
s.strip().split()  # <-- you will probably see this, old python 2 artifact


"""
    Slicing of strings
    
        What is a slice? 
            you can take a substring or sublist using special bracket notations
            
            [start: stop]
            just like with range, goes up to but not including the stop
            [start: stop: step]
"""

a_big_string = 'ASDFZXCVBNMASDFGHJK'
print(a_big_string[2: 6])

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a_list[7: 12])

print(a_list[0: len(a_list): 2]) # select all of the even indices
print(a_list[1: len(a_list): 2]) # select all of the odd indices

my_string = 'turtles'
print(my_string[4:2000000])
print(my_string[1000:2000])  # if it doesn't work its just an empty string
print(a_list[500: 5000])

"""
    There are default values
    [ blank : number ] set the start to 0
    [number : blank ] sets the blank to the len(whatever it is)
    [:] [blank : blank] ??? 
"""

print(my_string[:4])
print(my_string[2:])
print(a_list[:])  # makes a copy of a list

d_list = list(a_list)  # makes a true copy
b_list = a_list[:]  # makes a true copy, different memory locations
c_list = a_list     # makes a reference same list, different variable names

b_list[4] = 18
print(a_list)
c_list[4] = 18
print(a_list)

"""
    Reverse a list with a slice
"""

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(num_list[::-1])
