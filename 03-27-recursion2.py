"""
Recursion is when a function calls itself.

    Every recursion in computer science needs a base case.
        Infinite recursion is actually impossible
        Causes a "stack overflow" meaning you run out of memory.
        Python has a limit of 1000 recursions

    We did a bunch of mathematical recursions:
        1 + 2 + 3 + ... + n = n(n + 1)/2
        1 * 2 * 3 * 4 ... * n = n! (no formula for this one sadly...)
        f(n) = f(n - 1) + f(n - 2)
            Problem with this [feature] is that it is a branching recursion
            A branching recursion is one where a recursive call makes more than
                1 recursive calls.
            On average each call makes 1.618 additional calls

    Are there any other examples of recursion?
        Of course, plenty...

        What if i wanted you to output all of the permutations of a's and b's that you
        can make of length 4?
        L = 0
            maybe this is the base case, we do nothing
        L = 1
        a       b
        L = 2
        aa  ab   ba   bb
        L = 3
        aaa  aab   aba   abb
        baa  bab   bba   bbb
        L = 4
        aaaa  aaab   aaba   aabb
        abaa  abab   abba   abbb
        baaa  baab   baba   babb
        bbaa  bbab   bbba   bbbb

"""


def make_as_and_bs(n, current=''):
    if n == 0:
        print(current, end='  ')
        return  # or you can do this
    else:
        make_as_and_bs(n - 1, current + 'a')  # starts with an a
        make_as_and_bs(n - 1, current + 'b')  # starts with a b


"""
    Instead of counting the number of as or bs i'm going to count 
    k = #a - #b >= 0
    
    The number of a's should be more or equal to the number of b's
"""


def make_as_and_bs_morea(n, k=0, current=''):
    if n == 0:
        if k >= 0:  # specifically greater than or equal to
            print(current, end='  ')
        return  # or you can do this
    else:
        make_as_and_bs_morea(n - 1, k + 1, current + 'a')  # starts with an a
        make_as_and_bs_morea(n - 1, k - 1, current + 'b')  # starts with a b


"""
                                M(4, '')
        M(3, 'a')                                   M(3, 'b')
M(2, 'aa')              M(2, 'ab')                  M(2, 'ba')                  M(2, 'bb')
M(1, 'aaa') M(1, 'aab')  M(1, 'aba') M(1, 'abb')    M(1, 'baa') M(1, 'bab')     M(1, 'bba')  M(1, 'bbb')
M(0, 'aaaa')  M(0, 'aaab') M(0, 'aaba') M(0, 'aabb') ... 12 more of these

"""

make_as_and_bs(4)
print()
make_as_and_bs(12)
print()
# make_as_and_bs(20)
print('\n\n')
make_as_and_bs_morea(4)
print()
make_as_and_bs_morea(8)
print('.')
make_as_and_bs_morea(5)
print('.')

"""

Pathfinding...

    We're on a 2d grid, there are walls, and there are edges that we cant cross
    **********
    *S  *    *
    *** *** **  
    *  X     *
    **** *****
    *  P     *
    **********

    We need a way to backtrack.  Recursion gives us this.  
    
    
    We need to make a grid.  Nothing to do with recursion we need the world that
        we will explore.  
"""

import random

WALL = '*'
SPACE = '_'
GOAL = 'G'


# p = probability of a wall = 0.3
def create_grid(height, width, p):
    the_grid = []
    for i in range(height):
        new_row = []
        for j in range(width):
            if random.random() < p:
                new_row.append(WALL)
            else:
                new_row.append(SPACE)
        the_grid.append(new_row)

    the_grid[0][0] = SPACE
    the_grid[random.randint(0, height - 1)][random.randint(0, width - 1)] = GOAL
    return the_grid


def display_board(the_board):
    print('\t', end='')
    for k in range(len(the_board[0])):
        print(f' {k} ', end='')
    print()
    for i in range(len(the_board)):
        print(i, '\t', end='')
        for j in range(len(the_board[i])):
            print(f" {the_board[i][j]} ", end='')
        print()


def pathfinding(the_board, x, y, visited):
    print(x, y)
    if the_board[x][y] == GOAL:
        return True

    # check to make sure we havent been here already if we have its not the way
    if [x, y] in visited:
        return False

    # add our current position to visited, so we never come back here.
    visited.append([x, y])

    found_up = found_down = found_left = found_right = False
    # simple and less wrong
    if x - 1 >= 0 and the_board[x - 1][y] != WALL:
        found_up = pathfinding(the_board, x - 1, y, visited)  # up
    if x + 1 < len(the_board) and the_board[x + 1][y] != WALL:
        found_down = pathfinding(the_board, x + 1, y, visited)  # down
    if y - 1 >= 0 and the_board[x][y - 1] != WALL:
        found_left = pathfinding(the_board, x, y - 1, visited)  # left
    if y + 1 < len(the_board[x]) and the_board[x][y + 1] != WALL:
        found_right = pathfinding(the_board, x, y + 1, visited)  # right

    return found_up or found_down or found_left or found_right


my_grid = create_grid(10, 10, 0.30)
display_board(my_grid)
print(pathfinding(my_grid, 0, 0, []))
