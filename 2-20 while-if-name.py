"""
if __name__ == '__main__':
"""

import main_example


def main():
    print('I am the main function I will run every time the program is called')


name = input('What is your name? ')

# functions go here

if __name__ == '__main__':
    print('all my code goes in here')
    print('why would we do this? ')
    print(globals())
    """
        When you have multiple python files in a program, 
            the first file gets run is called __main__
            any other file gets the file name
    
        main() is essentially the same as any other function, you have to call it
            not really a main function
        
        put all your testing code into the if name == main block
        
        You write this statement, and then all your code goes inside it.  
    """

if __name__ == "__main__":
    x = 3
    for i in range(100):
        x += 2 * i
    print(x)

"""
    While Loops
        We've talked about for loops, but for loops have a specific limitation
        
        for i in range(len(my_list)): indices between 0 -> len(my_list) - 1
        
        for x in my_string:
            spits out each character in the string
        
        for i in range(100):
            goes 100 times that's it.  
        
        Sometimes you need a loop to keep going until something happens.  
"""

password = 'abcd1234'

"""
test_pw = input('What is your password? ')

for i in range(5):
    if test_pw == password:
        print('Logged In.')
    else:
        print('Try Again.')
        test_pw = input('What is your password? ')
"""

"""
    Ask the same question until the user gives us the right data.

    while loops are really if statements on repeat
"""
test_pw = input('What is your password? ')
while test_pw != password:
    print('Try Again.')
    test_pw = input('What is your password? ')


"""
    user input validation = trap the user until they give you data that 
    won't cause problems
"""


"""
Remember that we guarantee that if you say enter an integer then we will do that
    but we may not enter a positive integer.  
    We won't intentionally cause a ValueError
    We can give you 0, negatives
    If you say, enter a non-empty string, or a string with a word of five letters
    we can enter a string of 3 letters.      
"""

# priming the input
x = int(input('Enter a positive integer: '))
while x <= 0:
    x = int(input('That was negative or zero. Enter a positive integer: '))

print(x ** (1/2), 5 / x)

my_word = input('Enter a five letter word: ')
while len(my_word) != 5:
    my_word = input('Please try again. Enter a five letter word: ')


if len(my_word) >= 5:
    print(my_word[0], my_word[4])

"""
    Hint: always check for empty strings or empty lists.  
"""

"""
    Other reasons that you might want to use a while loop:
        Do I know how many times the loop should run?
            No -> while 
            Yes -> For
    Tic Tac Toe, Chess, any game that doesnt have exactly 10 turns
        how many times does the game take turns? I don't know 
        Thats not how it works... probably while loop
"""

victory = False
turn_count = 0
while not victory:
    if turn_count % 2 == 0:
        print('it is player 1\'s turn.')
        if input('Did you win? ').lower() == 'yes':
            victory = True
    else:
        print('it is player 2\'s turn \" ')
        if input('Did you win? ').lower() == 'yes':
            victory = True
    turn_count += 1  # turn_count = turn_count + 1

"""
What is a checkmate in chess?
    go through all the pieces on one side and see if they're attacking the king in the
        next move
        if so that's called check.
    there then has to be no possible move that prevents it.  
"""

"""
    common applications of while loops:
        servers 
            somewhere in server code is a while loop
                it waits until the next message comes in from the internet
                determines how to respond, sends the response. 
                
        graphical user interfaces
            waits for you to type or click or tap
            it figures out what to do based on that
            does it.
            goes back up to the top and waits again
            WM_QUIT message
            destroy message usually for the main window
        menu programs...
            probably will make some of these.  
"""


x = 100
while x > 0:
    # 40 lines of code
    x -= 1
    print(x)

# for loops cannot be infinite, while loops can

"""
    95% of all loops you write will be for loops
    but the while loop will often be the most important in the program.  
"""

game_loop_string = """
Enter one of these:
1) New Game
2) Load
3) Save
4) Configure Settings
5) Quit
"""

option = int(input(game_loop_string))
while option != 5:
    print(f'You chose {option}')
    if option == 1:
        print('Let us start a new game')
    elif option == 2:
        print('Load a game')
    elif option == 3:
        print('Save a game')
    elif option == 4:
        print('Settings')

    option = int(input(game_loop_string))
