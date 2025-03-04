"""
1 C
2 D
3 C
4 C
5 B
6 B or C [oops, not intentional]
7 A
8 C
9 D
10 D
11 B
12 D
13

Caesar Sulla

14)

8           [ write this because it does print before the error happens]
IndexError [you only need to write error]

15)

 [”Varro”, ”Caesar”, ”Pompey”, ”Sulla”, ”Fabius”]

"""

print(int(float('0.0')))
float('8.217')
float('0.0')
# int('0.0') doesnt work

print([1, 2, 3] in [1, 2, 3, 4, 5])
print([1, 2, 3] in [[1, 2, 3], 4, 5])

"""

16. Write an expression that is True if and only if a string sentence 
contains ’silly’ as a substring and either silly factor is greater 
than 5 or grumpy factor is greater than 12.

17. Write an expression that is True if and only if a list named cats 
contains ’Felix’ and ’Garfield’ but does not contain ’Pupper’

What I mean by a boolean expression is the thing that goes inside of the if statement
"""
# you dont need to do this
sentence = ''
silly_factor = 87
grumpy_factor = 5
# this is the answer
'silly' in sentence and (silly_factor > 5 or grumpy_factor > 12)

cats = ['Felix', 'Garfield', 'Minion']
'Felix' in cats and 'Garfield' in cats and 'Pupper' not in cats

"""
18) The step size is positive, the start is bigger than the end, so the for loop 
    won't execute.  
    
19) Yes. 
    for x in my_list or for i in range(len(my_list))
        scribble 
        
    ==>
    i = 0
    while i < len(my_list):
        do the stuff  #once this grows to 20-30 lines of code
        i += 1  # so easy to accidentally delete this

20)
    start   stop    step
    start   stop
    stop
    dont explain
    
21)
    8 > 49
    False
22) 
    (False) or (True)
    True
23)
    True and True
    True

24)
1
2
3

25)
Well Hello There

26)
17
13
9
5

27)
Line 12, add colon
Line 15: Change from the_string[x] in bad_symbols to the_string[x] not in bad_symbols
Line 17: change to else
Line 18: removed_symbol += 1
Line 19: new_list.append(new_string)
Line 21: missing () on the join
"""

"""Sum or product: """

the_sum = 0
the_product = 1

while the_sum <= 100 and the_product <= 100:
    # x = int(input('num: '))
    x = int(input('Tell me the next number: '))
    the_sum += x
    the_product *= x
    print(the_sum, the_product)

print('We are done. ')

double_letter = False
double_letter_list = []
the_string = input('Enter a string: ')
for i in range(len(the_string) - 1):
    if the_string[i] == the_string[i + 1]:
        double_letter = True
        double_letter_list.append(the_string[i])

if double_letter:
    print('There is a double letter')
else:
    print('Nope')

nl = []
x = int(input('N: '))
while x != 0:
    nl.append(x)
    x = int(input('N: '))

for i in range(len(nl)):
    if nl[i] % 2 == 0:
        nl[i] = nl[i] ** 2

print(nl)

if __name__ == '__main__':
    string_list = []
    s = input(" Enter a string : ")
    while s != "stop":
        string_list.append(s.lower())
        s = input(" Enter a string : ")

    most_a_word = ''
    current_a_count = 0
    for word in string_list:
        count = 0
        for letter in word:
            if letter.lower() == 'a':
                count += 1
        if count > current_a_count:
            current_a_count = count
            most_a_word = word

    print(most_a_word, current_a_count)