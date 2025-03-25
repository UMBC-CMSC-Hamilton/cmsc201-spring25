import datetime
"""

There are three or four ways to read from a file

    .read() ==> reads the entire file
        .read(the number of characters/bytes) [not going to use that]
    file.readline() => reads an individual line
    file.readlines() => reads the entire file splits it into lines [as a list]
    for line in file:   => calls readline one at a time
        do something with the line

    none of these read methods remove the \n 's from the strings that it gives you
        sometimes you may have to call strip() on the strings

There are a few methods to write a file:
    file.write() writes an individual string into the file [you must insert newlines
        where you need them]
    file.writelines(a list of strings) writes that list of strings into the file
        also doesn't add newlines to the strings

"""
if False:
    write_file = open('test_write.txt', 'w')

    st = input('Tell me something to put into the file: ')
    while st != 'quit':
        write_file.write(st + '\n')
        st = input('Tell me something to put into the file: ')

    write_file.close()  # important so that the file doesn't end up locked up


    with open('another_test.txt', 'w') as another_file:
        # the one advantage of this is that it will automatically close your file
        # i don't have to remember to close the file
        the_lines = []

        st = input('Tell me something to put into the file: ')
        while st != 'quit':
            the_lines.append(st + '\n')
            st = input('Tell me something to put into the file: ')

        another_file.writelines(the_lines)

"""
    The write mode will blank the file.  
    
        Remember to add the newline at the end of the strings, where you want them
"""

"""
    Last mode we're going to talk about is append mode
    
    log files, very important are the primary use for this
"""

with open('log_file.txt', 'a') as the_log:

    st = input('What happened?')

    while st != 'quit':
        the_log.write(f"{datetime.datetime.now()}" + st + '\n')
        st = input('What happened?')

"""
Append mode puts the cursor at the end of the file and doesn't overwrite the data
inside of the file.  
"""