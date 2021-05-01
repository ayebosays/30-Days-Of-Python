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

# formatted_string = 'I am %s %s. I am also a %s' %(firstName, lastName, suffix)
# print(formatted_string)

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of a circle with a radius of %d is %.2f.' %(radius, area) # 2 refers to 2 significant digits after the decimal point
# print(formated_string)

# python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
# form_string = 'The following are python libraries:%s' %(python_libraries)
# print(form_string)

# # New Style String Formatting (str.format)
# major = 'Computer Scientist'
# new_formatted_string = 'Hello, my name is {} {}. I am a {}'.format(firstName, lastName, major)
# print(new_formatted_string)

# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))       # 7
# print('{} - {} = {}'.format(a, b, a - b))       # 1
# print('{} / {} = {:.2}'.format(a, b, a / b))    # limit it to two digits after decimal, 1.33
# print('{} * {} = {}'.format(a, b, a * b))       # 12
# print('{} % {} = {}'.format(a, b, a % b))       # 1
# print('{} // {} = {}'.format(a, b, a // b))     # 1
# print('{} ** {} = {}'.format(a, b, a ** b))     # 64

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_string = 'Area of a circle with raidus {} is {:.2f}.'.format(radius, area) # 2 digits of precision
# print(formatted_string)

# String Interpolation / f-String (python 3.6+)
#
# Another new string formating, f-strings. Strings start with f and we can inject the data
# in their corresponding positions
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} / {b} = {a / b:.2f}')       # 2 digits of precision after decimal point
print(f'{a} * {b} = {a * b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')