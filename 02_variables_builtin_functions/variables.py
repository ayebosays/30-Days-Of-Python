# Day 2: 30 Days of python programming

# Exercise: Level 1

firstName = 'Abel'
lastName = 'Castillon'
fullName = firstName + lastName
country = 'United States'
city = 'Indio'
age = 32
year = 2021
is_married = False
is_true = True
is_light_on = True
is_male, is_tall, is_on_computer = True, True, True

# Exercise: Level 2

# 1. Check the data type of all your variables using type() built-in function
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_male))
print(type(is_tall))
print(type(is_on_computer))

# 2. Using the len() built-in function find the length of your last name
print(len(firstName))

# 3. Compare the length of your first name and your last name
print(len(firstName), len(lastName))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#   - Add num_one and num_two and assign the value to a variable _total
_total = num_one + num_two
print(_total)

#   - Subtract num_two from num_one and assign the value to a variable _diff
_diff = num_two - num_one
print(_diff)

#   - Multiply num_two and num_one and assign the value to a variable _product
_product = num_two * num_one
print(_product
)
#   - Divide num_one by num_two and assign the value to a variable _division
_division = num_one / num_two
print(_division
)
#   - Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
_remainder = num_two % num_one 
print(_remainder)

#   - Calculate num_one to the power of num_two and assign the value to a variable _exp
_exp = num_one ** num_two
print(_exp
)
#   - Find floor division of num_one by num_two and assign the value to a variable _floor_division
_floor_division = num_one // num_two
print(_floor_division)

# 5. The radius of a circle is 30 meters
radius_of_circle = 30
pi = 3.14

#   - Calculate the area of a circle and assign the value to a variable area_of_circle
#   area formula: (pi * radius) ** 2
area_of_circle = (radius_of_circle ** 2) * pi
print(area_of_circle)

#   - calculate the circumference of a circle and assign the value to a variable circum_of_circle
#   - Take radius as user input and calculate the area

circum_of_circle = ((pi * radius_of_circle) * 2)
print(circum_of_circle)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their
#    corresponding variable names
firstName = input('Enter first name: ')
lastName = input('Enter last name: ')
country = input('Enter country name: ')
age = input('Enter age: ')
print(firstName)
print(lastName)
print(country)
print(age)

# 7. Run help('keywords') in python shell or in your file to check the reserved words
"""Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield"""