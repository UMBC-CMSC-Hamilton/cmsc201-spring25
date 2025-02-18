"""
    What is a for loop?
        it is a loop that allows us to repeat a piece of code
        based on either an index or an element

        Two kinds of for loops:
            for-i[ndex] loops = use indices, for i in range(len(a_list))
                length = len(list or string or dictionary)
                for index in range(length):

            for-each loop = uses elements of a string, list, or some other object
                for c in my_string:
                    each character from the string will appear as c
                for x in my_list:
                    each element in my_list will appear as x
                for i in my_numbers:
                    print(i) = for each loop

            Two reasons you might need for-i[ndex] loop
                1) You might need to modify the elements
                2) You care about the positions in the list or string

    If you are at position i, the next position is i + 1
"""
if False:
    my_string = 'hello there'

    for c in my_string:
        if c != 'h':
            print(c)
            c = 't'

    print(my_string)

    my_list = [1, 2, 3, 6, 9, 12]

    for i in my_list:
        print(i + 2)
        i = 17

    print(my_list)


    for i in range(len(my_list)):
        print(i, my_list[i])
        my_list[i] = 17

    print(my_list)

    my_integers = [2, 3, 7, 9, 12, 15, 17, 18, 20, 22]
    # i want to check if the number and its neighbor are both even or both odd


    # if you change i + 1 to i + 2 then you need to change the len - 1 to len - 2
    for i in range(len(my_integers) - 1):
        if my_integers[i] % 2 == 0 and my_integers[i + 1] % 2 == 0:
            print(f'At {i} and {i + 1} they are both even')
        elif my_integers[i] % 2 != 0 and my_integers[i + 1] % 2 != 0:
            print(f'At {i} and {i + 1} they are both odd')

    """
        Drawing 2d-shapes
        
        Draw a rectangle
    """
    height = int(input('Enter the height: '))
    width = int(input('Enter the width: '))

    for y in range(height): # prints each line in sequence
        for x in range(width):  # prints a single line
            # print automatically shoves in a newline at the end of a print call
            # end="" changes the end from "\n" to ""
            print('*', end='')
        print()  # automatically resets end='\n'



    for y in range(height): # prints each line in sequence
        for x in range(height):  # prints a single line
            if x <= y:
                print('*', end='')
        print()  # automatically resets end='\n'

    for y in range(height): # prints each line in sequence
        for x in range(height):  # prints a single line
            if x >= height - 1 - y:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # automatically resets end='\n'


    for y in range(height): # prints each line in sequence
        for x in range(width):  # prints a single line
            if x == 0 or x == width - 1:
                print('*', end='')
            elif y == 0 or y == height - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # automatically resets end='\n'

    line_string = ''
    print('\n\n\n')
    for y in range(height):  # prints each line in sequence
        line_string = ''
        for x in range(width):  # prints a single line
            if x == 0 or x == width - 1:
                line_string += '*'
            elif y == 0 or y == height - 1:
                line_string += '*'
            else:
                line_string += ' '
        print(line_string)  # automatically resets end='\n'


    # draw a circle
    # (x - a)^2 + (y - b)^2 = r^2 center = (a, b) = (0,0)
    # x^2 + y^2 = r^2

    radius = int(input('What is the radius of the circle? '))

    tolerance = 0.5
    for y in range(-radius, radius + 1):  # prints each line in sequence
        for x in range(-radius, radius + 1):  # prints a single line
            if (radius - tolerance) ** 2 <= x ** 2 + y ** 2 <= (radius + tolerance) ** 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()


"""
    Remove, you need it for a hw problem, so I better teach it...

    Two ways to remove elements from a list:
        1) by element <--
        2) by index
"""

test_list = [2, 5, 7, 8, 9, 10, 13, 11, 5, 7]
if 5 in test_list:
    test_list.remove(5)  # removes the first element in the list that matches
print(test_list)
if 5 in test_list:
    test_list.remove(5)
print(test_list)
if 5 in test_list:
    test_list.remove(5)

"""
If you want to remove by index:
    del keyword
"""

del test_list[4]
print(test_list)

remove_index = int(input('Which index do you want to remove? '))
if 0 <= remove_index < len(test_list):
    del test_list[remove_index]
else:
    print('That was not in range. ')

print(test_list)

print()
new_list = [1, 2, 5, 5, 6, 7, 5, 5, 9, 5]
for x in new_list:
    print(x, new_list)
    if x == 5:
        new_list.remove(5)


print(new_list)

num_deleted = 0
new_list = [1, 2, 5, 5, 6, 7, 5, 5, 9, 5]
for x in range(len(new_list)):
    print(x, new_list)
    if x - num_deleted < len(new_list) and new_list[x - num_deleted] == 5:
        del new_list[x - num_deleted]
        num_deleted += 1

print(new_list)

new_new_list = []
for x in range(len(new_list)):
    if new_list[x] != 5:
        new_new_list.append(new_list[x])

print(new_new_list)