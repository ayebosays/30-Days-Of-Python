# Exercises - Day 3 - Operators

# 1. Declare your age as integer variable
age = 32

# 2. Declare your height as a float variable
height = 5.6

# 3. Declare a complex number variable
_complex = 1 + 2j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
base = float(input('Enter the base of the triangle: '))
_height = float(input('Enter the height of the triangle: '))
area = (0.5 * base * _height)
print('Area: ', area)

# 5. Write a script that prompts the user to enter side a, side b, side c of the triangle.
#    Calculate the perimeter of the triangle (perimeter = a + b + c)
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perimeter = (side_a + side_b + side_c)
print('Perimeter: ', perimeter)

# 6. Get length and width of a rectangle using prompt.
#    Calculate its area (area = length x width) and perimeter (perimeter = 2x (length + width))
_length = float(input('Enter a length: '))
_width = float(input('Enter a width: '))
_perimeter = 2 * (_length + _width)
print('Perimeter: ', _perimeter)

# 7. Get radius of a circle using prompt.
#    Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
_radius = float(input('Enter a radius: '))
pi = 3.14
_area = float((pi * _radius * _radius))
print('Area: ', _area)
_circumference = float((2 * pi * _radius))
print('Circumference: ', _circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = (2x - 2)
#    slope intercept equation: y = m x + b
#    y is y_coordinate
#    m is slope
#    x is x_coordinate
#    b is y_intercept
x_coordinate = float(input('Enter x-coordinate: '))
y_coordinate = float(input('Enter y-coordinate: '))
_b = float(input('Enter y-intercept: '))
_m1 = float((y_coordinate - _b) / x_coordinate)
print('slope: ', _m1)

x_coordinate = float((y_coordinate - _b) / _m1)
print('x-coordinate: ', x_coordinate)

_b = float(((_m1 * x_coordinate) + _b))
print('y-intercept: ', _b)

# 9. Slope is (m = (y_2 - y_1) / (x_2 - x_1)).
#    Find the slope between point (2, 2) and point (6, 10)
x_1 = int(input('Enter x_1: '))
y_1 = int(input('Enter y_1: '))
x_2 = int(input('Enter x_2: '))
y_2 = int(input('Enter y_2: '))
_m2 = float((y_2 - y_1) / (x_2 - x_1))
print('slope: ', _m2)

# 10. Compare the slopes in tasks 8 and 9.
print('slope 1: ', _m1)
print('slope 2: ', _m2)

# 11. Calculate the value of y(y = x^2 + 6x + 9).
#     Try to use different x values and figure out at what x value y is 0.
_x = int(input('Enter a x value: '))
_y = int(input('Enter a y value: '))
_y = _x ** 2 + 6 * _x + 9
print('y = x^2 + 6x + 9')
print(_y)


# 12. Find the length of 'python' and 'jargon' and make a falsy comparison statement.
phrase_1 = len('python')
phrase_2 = len('jargon')
# should print True because they're equal length
print(phrase_1 == phrase_2)
print('phrase_1 length: ', phrase_1)
print('phrase_2 length: ', phrase_2)

# 13. Use and operator to check if 'on' is found in both 'python' and 'jargon'
_on = 'on'
_python = 'python'
_jargon = 'jargon'
print(_on in _python and _on in _jargon)


# 14. I hope this course is not full of jargon.
#     Use in operator to check if jargon is in the sentence.
_sentence = 'I hope this course is not full of jargon'
print(_jargon in _sentence)

# 15. There is no 'on' in both dragon and python
dragon = 'dragon'
python = 'python'
print(_on not in dragon and _on not in python)

# 16. Find the length of the text python and convert the value to float and convert it to string
print('length of python as float: ', float(len('python')))
print('length of python as string: ', str(len('python')))

# 17. Even numbers are divisible by 2 and the remainder is zero.
#     How do you check if a number is even or not using python?


# 18. The floor division of 7 by 3 is equal to the int converted value of 2.7.

# 19. Check if type of '10' is equal to 10

# 20. Check if int('9.8') is equal to 10

# 21. Write a script that prompts the user to enter hours and rate per hour.
#     Calculate pay of the person?
hours = float(input('Enter number of hours: '))
ratePerHour = float(input('Enter rate per hour: $ '))
pay = hours * ratePerHour
print('Your pay: $ ', pay)

# 22. Write a script that prompts the user to enter number of years.
#     Calculate the number of seconds a person can live.
#     Assume someone lives up to hundred years
secondsInMinute = 60
minutesInHour = 60
secondsInAHour = (secondsInMinute * minutesInHour)
print('Seconds in an hour: ', secondsInAHour)
hoursInDay = 24
secondsInADay = (secondsInAHour * hoursInDay)
print('Seconds in a day: ', secondsInADay)
daysInYear = 365
secondsInAYear = (secondsInADay * daysInYear)
print('Seconds in a year: ', secondsInAYear)
numOfYears = input('Enter number of years you have lived: ')
secondsToNumberOfYears = (numOfYears * secondsInAYear)
print('You have lived for ', secondsToNumberOfYears)

# 23. Write a python script that displays the following table
#
#     1 1 1 1 1
#     2 1 2 4 8
#     3 1 3 9 27
#     4 1 4 16 64
#     5 1 5 25 125
