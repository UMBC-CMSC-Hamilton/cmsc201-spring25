"""
1) C
2) C
3) B
4) A
5) C
    if key in my_dict:
        my_dict[key]
    if the question was my_dict.get(key) not in the dictionary -> returns None
    my_dict.get(key, default_value) if its not there it'll return -> default_value
6) B
7) C
8) B <-- but maybe a little A too...
9) A
10) 3 + 6 = 9
11) KeyError
12) { ’ falafel ’: 3 , ’ quiche ’: 6 , ’ babka ’: 6, ’ danish ’: 5}
13) 8
14) grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X'

  0 1 2
0 X _ _
1 _ X _
2 _ _ X

15) Write an expression that evaluates to True if and only if a dictionary named robots has a
key ‘Data’ and a key ‘HAL’ but not the key ‘Marvin’.

'Data' in robots and 'HAL' in robots and 'Marvin' not in robots

16)
No base case:
In Theory: the recursion will call itself forever [infinitely] until either you run out of memory, or
    if we are theoretical enough, forever.

In Python: RecursionError <- after about 1000 recursions.

17)
You must check that:
[-len(grid)] 0 <= row < len(grid)
You must also check:
[-len(grid[row]) 0 <= col < len(grid[row])
grid[row][col]

17-function)
    function name, [arguments or parameters], definition/declaration/instantiation, call, body [code]

18) show some work:
c = 8
inner(4, 8) = 28
outer(28, 3)
d = 34

ans:
4 3 8 34

19)
def diabolical (n , k ):
    print (n , k )
    if n < 1:
        return 1
    return 1 + diabolical ( n - k , k + 1)

print ( diabolical (25 , 0))

25 0 -> 1 + d(25 - 0, 1)
25 1 -> 1 + d(24, 2)
24 2 -> 1 + d(22, 3)
22 3 -> 1 + d(19, 4)
19 4 -> 1 + d(15, 5)
15 5 -> 1 + d(10, 6)
10 6 -> 1 + d(4, 7)
4  7 -> 1 + d(-3, 8)
-3 8 -> returns 1
9

d(25, 3)
d(22, 4)
d(18, 5)
d(13, 6)
d(7, 7)
d(0,0)
"""

# 20)

print('hellojelloyellow'.split('ll'))
ans = ['he', 'oje', 'oye', 'ow']

print('aabaxa'.split('a'))

# 21)

matrix = [[5, 4, 3], [7, 8, 9], [2, 1, 0]]
for i in range(3):
    print(matrix[(2 * i + 1) % 3][(5 * i + 2) % 3])

# matrix[1][2] = 9
# matrix[0][1] = 4
# matrix[2][0] = 2
# ans: 9 4 2

"""
22. Convert the binary number 0011 0111 to decimal.
1 + 2 + 4 + 16 + 32 = 55

23. Convert the binary number 1010 0011 to decimal.
1 + 2 + 32 + 128 = 163

24. Convert the decimal number 53 to binary.
53 (odd) => 26 (even) => 13 (odd) => 6 (even) => 3 (odd) => 1 (odd)
0011 0101

25. Convert the decimal number 220 to binary.
220 (even) => 110 (even) => 55 (odd) => 27 (odd) => 13 (odd) => 6 (even) => 3 (odd) => 1 (odd)
1101 1100
128 + 64 + 16 + 8 + 4 = 220
"""

"""
12) Add range to the loop, convert to full for i loop
14) missing colon
16) if c in switches:
19) new_line += c
20) new_lines.append(new_line)
22) new_lines.append(lines[row])

"""


# = 0 only works when you dont pass the parameter
def sum_ascending(L, current=0):
    if not L:
        return 0

    if L[0] > current:
        return L[0] + sum_ascending(L[1:], L[0])
    else:
        return sum_ascending(L[1:], current)


# there were other ways...

sum_ascending([1, 2, 1, 4, 1, 6, 7, 4, 9])


def max_of_lists(L):
    max_list = []
    for row in L:
        if row:
            max_val = row[0]  #  0 but only for positive lists
            for val in row:
                if val > max_val:
                    max_val = val
        else:
            max_val = 0

        max_list.append(max_val)

    return max_list