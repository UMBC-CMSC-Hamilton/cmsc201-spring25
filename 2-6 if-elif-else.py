"""
    remember last time if you want to branch, you can use an if statement

    you can also use elif as "else if" when the if statement is false it checks
        the elif statements until it finds a true one

    you can also include an else, which occurs if all of the statements are false


"""
x = int(input('What is x? '))
if x == 3:
    print('hi')
else:
    print('something else')

"""
    Specific to the more general
    specific cases are the ones you want to catch first and handle differently
    the more general cases you can handle those if the specific case doesn't fire off
"""
# keep using x
if x > 0:
    print('x is positive')
elif x == 4:
    print('4 is a square')
elif x == 25:
    print('25 is also a square')

print('Second Statement: ')
if x == 4:
    print('4 is a square')
elif x == 25:
    print('25 is also a square')
elif x > 0:
    print('x is positive')


name = input('What is your name? ')
pin = int(input('What is your pin? '))

if name == 'Eric' and pin == 1588:
    print('You got them both correct. ')
elif name == 'Eric' or pin == 1588:
    print('You have got either name or pin correct')
else:
    print('Both are incorrect')


"""
Truth Tables for And, or , not

A and B
A\B     True    False

True    True    False
False   False   False


A or B [inclusive]
A\B     True    False
True    True    True
False   True    False

and and or are called 'binary operators'

not A
A       True    False
not A   False   True
"""

"""
Algebra of boolean operators

not executed first [not has a higher precedence]
and / or are executed at the same time
"""

a = True
b = False
print(not b or a)  # -b + a
print((not b) or a)  #  (not False) or True = True or True = True
print(not (b or a))  # not (False or True) =  not True = False

# not has a higher precedence than or/and but when you're coding you should
# use parentheses if you're 2% confused

c = True
d = False
print((a or b) and (not c or d))


"""
    Order of precedence inside of an if statement:
    
    Algebra - go first
        PEDMAS
        Left->Right
    Comparisons - go next
        ==, <=, >=, <, >, !=
    Logical Operators
        not - first
        and/or - second
"""
y = 5
print(x + 2 < y - 3 and x ** 2 < 50)
print((a and b) or (c and not d))

a = False
b = False
c = True
print(1, a and b or c, c or a and b)
print(2, (a and b) or c, c or (a and b))
print(3, (a and (b or c)))


"""
    Nesting:
        inside of if statements you can put if statements (elif, else)
        
        nesting is accomplished by tab-level.
        any tab level is permitted
        try to keep it under 6-8
"""

"""
20 questions Star Wars edition.  
"""
human = input('Are you human? ')
if human.lower() == 'yes':
    jedi = input('Are/were you a force user? ')
    if jedi.lower() == 'no':
        cloud_city = input('Did you run cloud city? ')
        if cloud_city.lower() == 'yes':
            print('You are Lando Calrissian')
        else:
            print('You are Han Solo')
    elif jedi.lower() == 'yes':
        dark_or_light = input('Light side or Dark? ')
        if dark_or_light == 'dark':
            love_dem = input('How do you feel about democracy? ')
            if love_dem == 'love':
                print('You are Palpatine, unlimited power...')
            else:
                print('You are Vader/Anakin')
        else:
            hate_farm = input('Do you hate moisture farming? ')
            if hate_farm == 'yes':
                print('you are luke')
            else:
                princess = input('Are you a princess? ')
                if princess.lower() == 'yes':
                    print('You are Leia')
                else:
                    print('You are Obi Wan, hello there.')
    else:
        print('Gonk droid...')
else:
    droid = input('Are you a droid? ')
    if droid.lower() == 'yes':
        bad_feeling = input('Do you have a bad feeling about nearly everything? ')
        if bad_feeling.lower() == 'yes':
            print('You are C-3P0')
        else:
            print('You are R2D2')
    else:
        print('You are Chewie')


"""
    Modulus Division
    
    Remember back to elementary school, you learned that
    17 / 5 = 3 R 2
    
    There's three types of division
    / = floating point division 17 / 5 = 3.4
    // = integer division  17 / 5 = 3, 18/5 = 3, 19/5 = 3, 20/5 = 4
    
    % modulus division, 17 % 5 = 2 [gives you the remainder from the division]
    
    7 % 3 = 1
    9 % 7 = 2
    25 % 4 = 1
    27 % 4 = 3
    28 % 4 = 0
    15 % 5 = 0
    check if things are even
    x % 2 == 0 [even]
    x % 2 == 1 [odd]
"""