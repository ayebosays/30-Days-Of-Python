# # Exercises - Day 4 - Strings

# # Text is a string data type.
# # Any data type written as text is a string.
# # Any data under single or double quotes are strings.

# # Creating a String
# letter = 'p'
# print(letter)

# # To check the length of a string use the len() method
# print(len(letter))

# # A multiline string is created using triple single ''' or double """ quotes
# multiline_string = '''I am a computer science graduate that is currently focusing on programming.
# My goal is to develop my programming portfolio with quality, creative, and well-thoughtout show pieces.
# Although I may not have the (2-3 years) of work experience necessary to land a software development job, I hope to use my work at a substitute to show my worth.'''
# print(multiline_string)

# # String Concatenation is merging or connecting strings together
# firstName = 'Abel'
# lastName = 'Castillon'
# suffix = 'Jr.'
# space = ' '
# fullName = firstName + space + lastName + space + suffix # concatenating strings
# print('My name is, ', fullName)

# print(len(firstName))   # 4
# print(len(lastName))    # 9
# print(len(firstName) > len(lastName)) # False - 4 !> 9
# print(len(fullName))    # 18

# # Escape Sequences in Strings
# #   \n: New line
# #   \t: Tab means(8 spaces)
# #   \\: Back slash
# #   \': Single quote (')
# #   \": Double quote (")

# print('30-Days-of-Python challenge has been a great experience.\nHoping for the best outcome') # line break
# print('Days\tTopics\tExercises')
# print('Day 1\t3\t5')
# print('Day 2\t3\t5')
# print('Day 3\t3\t5')
# print('Day 4\t3\t5')
# print('This is a backslash symbol \\') # To write a backslash
# print('In every programming langugage it starts with \"Hello, World!\"')

# # String Formatting
# # % operator is used to format a set of variables enclosed in a tuple(a fixed size list),
# #   together with a format string, which contains normal text together with "argument specifiers,"
# #   special symbols like %s, %d, %f, %.f
# #
# #   %s  - String(or any object with a string represenation, like numbers)
# #   %d  - Integers
# #   %f  - Floating point numbers
# #   %.f - Floating point numbers with fixed precision

# # formatted_string = 'I am %s %s. I am also a %s' %(firstName, lastName, suffix)
# # print(formatted_string)

# # radius = 10
# # pi = 3.14
# # area = pi * radius ** 2
# # formated_string = 'The area of a circle with a radius of %d is %.2f.' %(radius, area) # 2 refers to 2 significant digits after the decimal point
# # print(formated_string)

# # python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
# # form_string = 'The following are python libraries:%s' %(python_libraries)
# # print(form_string)

# # # New Style String Formatting (str.format)
# # major = 'Computer Scientist'
# # new_formatted_string = 'Hello, my name is {} {}. I am a {}'.format(firstName, lastName, major)
# # print(new_formatted_string)

# # a = 4
# # b = 3

# # print('{} + {} = {}'.format(a, b, a + b))       # 7
# # print('{} - {} = {}'.format(a, b, a - b))       # 1
# # print('{} / {} = {:.2}'.format(a, b, a / b))    # limit it to two digits after decimal, 1.33
# # print('{} * {} = {}'.format(a, b, a * b))       # 12
# # print('{} % {} = {}'.format(a, b, a % b))       # 1
# # print('{} // {} = {}'.format(a, b, a // b))     # 1
# # print('{} ** {} = {}'.format(a, b, a ** b))     # 64

# # radius = 10
# # pi = 3.14
# # area = pi * radius ** 2
# # formatted_string = 'Area of a circle with raidus {} is {:.2f}.'.format(radius, area) # 2 digits of precision
# # print(formatted_string)

# # String Interpolation / f-String (python 3.6+)
# #
# # Another new string formating, f-strings. Strings start with f and we can inject the data
# # in their corresponding positions
# a = 4
# b = 3
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} / {b} = {a / b:.2f}')       # 2 digits of precision after decimal point
# print(f'{a} * {b} = {a * b}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')

# # Python Strings as Sequences of Characters
# #
# # Python strings are sequences of characters, and shre their basic methods of access with other Python
# # ordered sequences of objects - lists, and tuples. The simplest way of extracting single characters
# # from strings (and individual members from any sequence) is to unpack them into corresponding variables.

# # Unpacking Characters
# language = 'python'
# a, b, c, d, e, f = language # unpacking sequence of characters into variables
# print(a)    # p
# print(b)    # y
# print(c)    # t
# print(d)    # h
# print(e)    # o
# print(f)    # n

# # Accessing Characters in Strings by Index
# #
# # In programming, counting starts from zero. Therefore, the first letter of a string is at index zero
# # and the last letter of a string is the length of a string minus one.
# #
# # Ex: ['P', 'y', 't', 'h', 'o', 'n']
# # index 0    1    2    3    4    5
# # length = 6 because 0,1,...5
# len_language = len(language)
# print('length of python is: ', len_language)

# first_letter = language[0]
# print('first letter: ', first_letter)
# second_letter = language[1]
# print('second letter: ', second_letter)

# # To access the last letter we can count backwards from -1
# last_letter = language[-1]
# second_to_last_letter = language[-2]
# print('last letter: ', last_letter)
# print('second to last letter: ', second_to_last_letter)

# # Slicing Python Strings
# #
# # we can slice strings into substrings
# first_half = language[0:3] # starts at zero index and up to 3 but not including 3, 0 >= 2
# last_half = language[3:6]
# print(first_half)
# print(last_half)

# # we can also access them from the opposite direction
# last_three = language[-3:]  # makes sense
# print(last_three)           
# last_three = language[3:]   # also works
# print(last_three)           

# # Reversing a String
# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleH

# # Skipping Character While Slicing
# #
# # It is possible to skip characters while slicing by passing step arguments to slice method
# language = 'python'
# pto = language[0:6:2] # [start, stop, step]
# print(pto)

# String Methods
#
# capitalize(): Converts first character of string to capital letter
# count(): returns occurrences of substrings in string, count(substring, start=, end=)
# endswith(): checks if a string ends with a specified ending
# expandtabs(): replaces tab character with spaces, default tab size is 8. Takes tab size argument
# find(): returns the lowest index of the first occurence of a substring, if not returns -1
# rfind(): returns the highest index of the first occurrence of a substring, if not returns -1
# format(): a variable string substitution { <variable> },...{ <variable> }.format(<variable(s)>) 
#           also works with f'string format
# index(): returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length -1)
# rindex(): returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length -1)
# isalnum(): checks if a character is alphanumeric, returns True or False
# isalpha(): checks if all string elements are alphabet characters (a-z and A-Z), returns True or False
# isdecimal(): checks if all characters in a string are decimela (0-9)
# isdigit(): checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# isnumeric(): checks if all characters in a string are numbers or number related (similar to isdigit(), accepts more symbols)
# isidentifier(): checks for a valid identifier -- if a string is a valid variable name
# islower(): checks if all characters in the string are lowercase 
# isupper(): checks if all characters in the string are uppercase
# join(): returns a concatenated string
# strip(): removes all given characters starting from the beginning and end of the string
# replace(): replaces substring with a given string
# split(): splits the string, using given string as a seperator
# title(): returns a title cased string
# swapcase(): conversts all uppercase characters to lowercase and all lowercase characters to uppercase characters
# startswith(): checks if string starts with a the specified string


# # Exercises - Day 4
# # 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# word_1 = 'Thirty'
# word_2 = 'Days'
# word_3 = 'Of'
# word_4 = 'Python'
# phrase = word_1 + ' ' + word_2 + ' ' + word_3 + ' ' + word_4
# print(phrase)

# # Another way
# words = [word_1, word_2, word_3, word_4]
# result = ' '.join(words)
# print(result)

# # 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# word_1 = 'Coding'
# word_2 = 'For'
# word_3 = 'All'
# phrase = word_1 + ' ' + word_2 + ' ' + word_3
# print(phrase)

# # Another way
# words = [word_1, word_2, word_3]
# result = ' '.join(words)
# print(result)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print('length of company name:', len(company))

# Change all the characters to capital letters using upper() method.
print(company)
print('using .upper()', company.upper())

# Change all the characters to lowercase letters using lower() method.
print('using .lower()', company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('\n')
print('using .capitalize()', company.capitalize())
print('using .title()', company.title())
print('using .swapcase()', company.swapcase())

# Cut(slice) out the first word of Coding For All string.
#
# C o d i n g _ F o r _  A  l  l
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
company = 'Coding For All'
slice_company_first_word = company[6:14]
print(slice_company_first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Replace the word coding in the string 'Coding For All' to Python.
# Change Python for Everyone to Python for All using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.
# Use a tab escape sequence to write the following lines.
#   Name    Age     Country
#   Abel    32      United States
# Use the string formating method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 square meters
# Make the following using string formating methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144