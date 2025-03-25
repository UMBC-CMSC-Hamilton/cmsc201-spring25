"""
Dictionaries

    Also called a Hash Table/Hash Map
        where the term hash tag comes from

    Different kind of data structure that allows us to store elements instead
        of using indices we use 'keys'

    Key is any immutable type: int, bool, string, float, datetime, tuple
        most of the time you'll be sticking to ints and strings

    Lists are kind of restricted because you need an index in order to access an element
        that index doesn't really mean anything
"""
my_hash = {}  # creates an empty dictionary
my_other_dict = dict()  # dictionary constructor

# inserting elements is done by assigning them the first time
my_hash['yellow'] = 15
my_hash['turtle'] = 2025
my_hash['robot'] = 91

print(my_hash['yellow'])

# if you access a key not in an assignment
# print(my_hash['squirrel'])
# this causes a KeyError
word = input('Tell me what to look up? ')
if word in my_hash:
    print(my_hash[word])
else:
    print('That was not in the dictionary.  ')

# if word not in my_hash:
#    print('some kind of error')


"""
Here's another way to test if something is in the dictionary

.get(key, value)

by default .get(key) returns None if it's not in the dictionary
"""

my_hash['cardinal'] = None
print(my_hash)
print(my_hash.get("turtle"), my_hash.get("sandwich"))

my_hash['bird'] = 7
print(my_hash.get("sandwich", -1))  # you arent using negatives,
# # then this will tell you that its not there

"""
How to remove something from a dictionary
"""

print(my_hash)
del my_hash['bird']  # be slightly careful with this
# del my_hash, I deleted the whole thing
print(my_hash)

"""
Why not to use floats as keys

    round off error, if you calculate a float in two different ways
        it can have two slightly different decimal expansions
        
"""
print(1 / 7, 8 / 7 - 1, 1 / 7 == 8 / 7 - 1)
my_other_dict[True] = 'happy'
my_other_dict[False] = 'sad'
# keep the same key type and the same value type whenever possible
mix_map = {'hi': 15, 3: 91, 'jello': 4, 5: 'syrup'}

# keys are strings [immutable] but the values are lists [mutable] (ok)
grades = {'eric8': [1, 2, 3, 4, 5],
          'blah2': [2, 3, 4, 5, 6],
          'adam7': [14, 21, 9, 3, 7],
          'blank4': []}

print(grades['eric8'])
print(grades['adam7'])

for key in my_hash:
    print(key, my_hash[key])

for username in grades:
    total = 0
    for i in range(len(grades[username])):
        total += grades[username][i]
    if len(grades[username]) > 0:
        print(username, 'has an average of ', total / len(grades[username]))
    else:
        print(username, 'has no grades')

# here's kind of the nightmare scenario for dictionaries with mutable keys
# why they don't do that in python
# watch out for this error [unhashable type] == mutable
# bad_list = [1, 2]
# my_other_dict[ bad_list ] = 7
# bad_list.append(3)

print(my_hash.keys())
# for key in my_hash.keys():

print(list(my_hash.values()))


# if you want to copy a dictionary you use the dictionary constructor
new_hash = dict(my_hash)
print(new_hash)
new_hash['cardinal'] = 77
print(new_hash)
print(my_hash)

"""
    Has nothing to do with dictionaries
    File IO = File Input/Output

   How do we open a file? 
"""

# open will return a "file object"
readme_file = open('readme.txt')
# reads the entire file - in your future life, this is dangerous, in 201 = ok
print(readme_file.read())
readme_file.close()

readme_file = open('readme.txt')
print(readme_file.read())
readme_file.close()

readme_file = open('readme.txt')
my_lines = readme_file.readlines()
for i in range(len(my_lines)):
    my_lines[i] = my_lines[i].strip()
print(my_lines)
readme_file.close()
"""
Leaves the newlines on, you can strip them off
"""


readme_file = open('readme.txt')
for line in readme_file:
    print('this is a line: ', line)

readme_file.close()

"""
The last read method: readline() [not readlineSSS]
"""
the_grid_file = open('griddy.txt')
dimensions = the_grid_file.readline()
print(dimensions)
dim_list = dimensions.split()
dim_list[0] = int(dim_list[0])
dim_list[1] = int(dim_list[1])
print(dim_list)

grid_data = the_grid_file.readlines()
if len(grid_data) != dim_list[0]:
    print('Error in data file.')

the_grid_file.close()
