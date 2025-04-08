"""
two dimensional list [higher dimensional list than 1]

a list inside of a list

"""

ex1 = [
    [1, 2, 3],  # index 0 list
    [3, 4, 5],  # index 1 list
    [9, 7, 6]  # index 2 list
]

ex2 = [[5], [123, 332, 2123], [234, 2, 2, 2, 2, 2, 2, 2], [1, 3, 5, 7]]

print(ex1[0], ex1[1], ex1[2])
print(ex1[0][1], (ex1[0])[1])
ex1[1][2] = 7
print(ex1)

"""
    notice that in ex2 there's an issue
    not all of the sublists are of the same length
    if you use the wrong length or accidentally use the len(ex2) on the inner loop
"""

for i in range(len(ex2)):  # length of the outer list
    for j in range(len(ex2[i])):  # length of the inner list  <<++ the most importand line of the lecture
        print(len(ex2[i]), ex2[i][j], end=" ")
    print()

for row in ex2:
    print(row)
    for element in row:
        print(element)

"""
    Sometimes you can get away with it becaues the number of rows == number of columns in each list
    
    When you have a board game, some kind of grid that you're working on.  
"""

"""
Let's say you wanted to build a rectangular grid.  rows = n, columns = m
"""
rows = int(input('How many rows do you want? '))
cols = int(input('How many columns do you want? '))

the_grid = []
# new_row = [] # what if we do this? then it's the same list for each row
for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append('*')
    the_grid.append(new_row)  # this puts a reference to the list not a copy into the_grid

for row in the_grid:
    print(' '.join(row))
for row in the_grid:
    print(' '.join(row))
print('Modifying [2][12] = a')
the_grid[2][2] = 'a'
for row in the_grid:
    print(' '.join(row))

# we dont really teach this
my_grid = [['*' for j in range(cols)] for i in range(rows)]  # this is currently banned
# this is extremely useful, you'll use it all the time
# most languages dont have them.


chess_board = []
for i in range(8):
    new_row = []  # what this does is tells the name new_row that now it points to [references] a new list which is empty
    for j in range(8):
        new_row.append('_')
    chess_board.append(new_row)

"""
higher dimensional lists
"""

three_d = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[3, 2, 1], [9, 8, 7], [3, 5, 9]],
    [[3, 2, 1], [9, 8, 6], [3, 5, 2]],
]

print(three_d[1][1][2])

"""
    Here's a mixed thing
"""

colors = ['red', 'green', 'blue', 'yellow']
deck = []
for i in range(10):
    for color in colors:
        new_card = {
            'number': i,
            'color': color
        }
        deck.append(dict(new_card))
        deck.append(dict(new_card))

print(deck)


def get_card_string(card):
    return card['color'] + str(card['number'])


for card in deck:
    print(get_card_string(card), end=", ")

print(deck[17]['color'], deck[17]['number'])

import random

random.seed(input('What is the seed? '))

random.shuffle(deck)
for card in deck:
    print(get_card_string(card), end=", ")

"""
    This deck is a list of dictionaries, kind of like a 2d list, but has a dictionary instead of an inner list

    You can make a 2d-dictionary
"""
gradebook = {
    'eric8': {'grades': [1, 2, 3, 4, 5], 'name': 'Eric'},
    'john2': {'grades': [2, 3, 4, 5, 6], 'name': 'Jonathan'}
}


for username in gradebook:
    total = 0
    for i in range(len(gradebook[username]['grades'])):
        total += gradebook[username]['grades'][i]

    print(username, total)
