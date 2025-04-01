"""

    recursive palindrome checker
        use slices

    If the first letter is equal to the last letter it's maybe a palindrome
    otherwise its not.

    What is the base case?
        '' a palindrome?? ==> yes
        'x' a palindrome? ==> yes
    Base case is going to be if the string is of the length <= 1 then it is automatically

"""


def rec_pal(a_string):
    print(a_string)
    if len(a_string) <= 1:
        return True

    if a_string[0] == a_string[-1]:  # len(a_string) - 1
        return rec_pal(a_string[1: -1])  # recursive case will go here, slice off the first and last character
    else:
        return False


my_string = input('Enter palindrome: ')
while my_string != 'quit':
    my_string = ''.join(my_string.split())
    print(rec_pal(my_string))
    my_string = input('Enter palindrome: ')


def count_as_rec(a_string):
    if not a_string:  # no as in an empty string so return 0
        return 0

    if a_string[0].lower() == 'a':
        # counts the rest of the a's adds 1
        return 1 + count_as_rec(a_string[1:])  # [1: len(a_string)]
    else:
        return count_as_rec(a_string[1:])


def find_replace(big_string, find_string, replace_string):
    """
        replace all instances of find_string with replace_string
    """
    print(big_string)
    if len(big_string) < len(find_string) or not find_string:
        return big_string

    if big_string[0: len(find_string)] == find_string:
        result = replace_string + find_replace(big_string[len(find_string):], find_string, replace_string)
        print(result)
        return result
    else:
        result = big_string[0] + find_replace(big_string[1:], find_string, replace_string)
        print(result)
        return result

print(find_replace('abcdrgsfjabcjflksabcsjfdlabc', 'abc', '0'))