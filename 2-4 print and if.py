"""
Declare a variable by assigning it the first time
    a variable is really a name linked with a place in memory [ram]
    more than one single location in ram, big sequence

Naming conventions in python?
    start with a letter or an underscore, not a number or symbol

    Coding standards, python allows more than just this
        we usually use lower case letters separated by underscores
        snake-case

    myVariableName - camel case, avoid this in python
    UsuallyLikeThis - capitalized case?? no idea
"""
if False:
    which_person = 'Robert'
    how_many = 17
    HOW_MANY = 18  # case sensitive, HOW_MANY is a different variable from how_many

    print(how_many, HOW_MANY)
    _like_this = 3
    __maybe_this = 'hello'
    ___crazy_but_maybe_not = 4

    ____ = 7
    print(____)

    """
    There are a lot of variable names that are allowed in python but not according 
        to the coding standards
    """
    rEaLlYWeIrD = 4
    """
    Snake case is really just lower case with underscores [all you need to know for now]
    """

    r527 = 527
    # 527r = 4
    binary_var = 0b101010101
    hex_var = 0xab12cef3442
    oct_var = 0o1237

    _123 = 'you could do this'
    """
        Try to make your variable names meaningful
        
        if you're using pycharm or some other ide you probably have autocomplete
    """

    num_plants = int(input('How many plants do you have? '))
    # num_plants = 4.79
    # num_plants = "plants"


    """
        Single letter variables are allowed when theyre in index of a loop
        or if it's some mathematical equation
    """

    """
        (-b + sqrt(b^2 - 4ac)) / (2a)
        (-b + sqrt(b^2 - 4ac)) / (2a)
        (-b+sqrt(b^2-4ac))/(2a)
    
        ^ = caret
        this caret means binary xor [bitwise]
        
        6 / 2 + 1 = 4
        6 / 2 ( 2 + 1 ) L -> R
        (3) * (3) = 9 [correct answer]
        obviously what i meant was 6  / (2 ( 2 + 1))
    """

    a = float(input('What is a? '))
    b = float(input('What is b? '))
    c = float(input('What is c? '))

    if a != 0:
        pos_root = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
        neg_root = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
        print(pos_root, neg_root)


    if b ** 2 - 4 * a * c >= 0:
        print('There are real roots')
    else:
        print('There are complex roots')



    num_movies = float(input('How many movies do you watch in a week? '))

    if num_movies < 0:
        print('That is not possible, you must watch many movies to get to zero. ')
    else:
        print('That is possible.  ')

    """
        Operators for numbers:
        
            == [equals, comparison not assignment]
            != [not equals]
            <= [if you use =< that will error]
            >= 
            <
            >
    """

    the_word = input('Tell me a word: ')

    if the_word.lower() == 'bird':  # you can use .lower() or .upper() to fix the strings
        print('Bird is the word')
    elif the_word == 'go':
        print('let\'s go')  # if you use \ backslash the next character can be ' "
    else:
        print('Something else')

    """
    In python, instead of using the keywords else if, they contracted them into 
    elif 
    
    if the first if statement is false, then it checks the first elif, then the next, and
        the next and the next
    """

    number = int(input('Tell me a number: '))

    if number == 1:
        print('1 is the loneliest number')
    elif number == 2:
        print('2 can be as bad as 1')
    elif number == 3:
        print('3 is either magic or a crowd')
    elif number == 4:
        print('4 is not prime, wow')
    else:
        print('That was something other than 1-4')

"""
Did I handle all of the cases?
    if there's unhandled cases do you want an else?
        maybe it depends
You can type as many elifs as you want [0 up to many]

"""

another_word = input('Another word: ')
if another_word.lower() < 'hello':
    print('yes')
else:
    print('no')

"""
    Encoding is ascii
        https://www.ascii-code.com/
"""