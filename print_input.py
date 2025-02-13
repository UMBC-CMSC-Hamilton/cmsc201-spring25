"""
have python, install it from python.org
    latest version is fine, anything after 3.7+ is also fine, you won't notice

Install PyCharm https://www.jetbrains.com/pycharm/download/
    Install the community edition, it's free

Install Bitvise - for windows.
https://cyberduck.io/download/ - for mac
"""

"""
Let's talk some python:
    Python is an interpreted language - runs in the python interpreter
    
    Whitespace SENSITIVE = it cares about spaces and tabs in some places
        uses them for scope, containment
    {} no such thing, sad
    
    Tabs or spaces? Big Python Debate
        in pycham it will convert all your tabs to 4 spaces each
    
    Fast for Development - user friendly language

Print and Input - they are built in python functions
    
"""

print('Hello World')
print("This is also a string that will be printed.  ")

"""
What other kinds of things can you print? 
integers - ..., -3, -2, -1, 0, 1, 2, 3, 4, 5, ... 
floating point number - 3.2, -8.1, 15.9, 0.23232323, 3.0 be careful with 3
booleans - True and False
and more we'll get to
"""

print(5, -2, 25, 125, 1919191, -303, 19827392183798721398172398127321)
print(3.14159265358979, 2.7182818459, -3.1, -55555.2, 5.0, 5)
print(type(5.0), type(5))
print(True, False)
print(True * True, True + 1, False * False)
# create a variable by assigning it
x = 3
print('the number is', x)
x = 'robots'
print(x)

y = 'yellow'
print(x + y)
# adding strings is called "concatenation"

z_string = "hello, i am a string with @#$%& characters 12356"

this_wont_work = 'this" '  # needs the end '
# comments can start with a pound sign, hash-tag, octothrope?

big_string = """
    This is both a string and a comment in a way... these are multiline strings
    if you dont assign it to a variable then it gets treated like a comment
    
    If it's obvious to you and you didnt think hard before writing that line
        no comment is necessary
    If you spent 5 minutes on that line of code, or more... comment
"""
print(big_string)


print(3 + int("7"), float("-4.59"), int(4.1), "7" + str(52))
print(4 + 7.8, 4 + int(7.8), int(3.99999999999), int(-5.2))
"""
By default, integer casting truncates the fractional part
"""
print(round(6.9232323, 3))
print(7.3432/2.91237813)

hat_count = 4
vegetable = 'turnip'

print(f"the number of hats is {hat_count} and the favorite vegetable is {vegetable}")
print("The number of hats is", hat_count, "and the favorite vegetable is", vegetable)

# This will generate a type error.
# print("The number of hats is: " + hat_count)

print("The number of hats is: " + str(hat_count))

"""
    input is also a built in function, takes a prompt, outputs a string (always a string)
"""

my_name = input("Tell me your name: ")
num_seals = int(input("How many seals are there? "))
print(type(num_seals))

favorite_decimal = input("What is your favorite float: ")
favorite_decimal = float(favorite_decimal)
print(favorite_decimal)


x = input("Some kind of string: ")

