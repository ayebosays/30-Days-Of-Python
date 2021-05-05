# Exercises - Day 5 - Lists

# Lists
#
# (4) collection data types
# 1. Lists: a collection which is ordered and changeable(modifiable). Allows duplicates. Can be empty or have different data typed items.
# 2. Tuple: a collection which is ordered and unchangable or unmodifiable(immutable). Allows duplicates
# 3. Set: a collection which is unordered, unindexed and unmodifiable, but you can add new items. Does not allow duplicates
# 4. Dictionary: a collection which is unordered, changeable(modifiable) and indexed. Does not allow duplicates

# How to Create a List
#
# Using list built-in function
_list = list()

empty_list = list()     # empty list, no items inside
print(len(empty_list))  # 0
print(len(_list))       # 0

# Using square brackets
_list = []
empty_list = []
print(len(_list))
print(len(empty_list))

# Lists with initial values. We use len() to find the length of a list
fruits = ['banana', 'apple', 'melon', 'pear']                                       # list of fruits
veggies = ['Potato', 'Cabbage', 'Onion', 'Celery']                                  # list of vegetables
animal_products = ['milk', 'eggs', 'meat', 'yogurt']                                # list of animal products
web_techs = ['HTML', 'CSS', 'JavaScript', 'ReactJS', 'Redux', 'Node.js', 'MongoDB'] # list of web technologies
countries = ['United States', 'Norway', 'Denmark', 'Sweden']                        # list of countries

# print the lists and their lengths
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', veggies)
print('Number of Veetables:', len(veggies))
print('Animal Products:', animal_products)
print('Number of Animal Products:', len(animal_products))
print('Web Technologies:', web_techs)
print('Number of Web Technologies:', len(web_techs))
print('Countries:', countries)
print('Number of Countries:', len(countries))

# Lists can have items of different data types
_list = ['Abel', 32, True, {'country':'United States', 'city':'Indio'}] # list containing different data types
print(_list)

# Accesssing List Items Using Positive Indexing
#
# We access each item in a list using their index. A list index starts from 0.
#
# ['banana', 'apple', 'melon', 'pear']
#     0         1        2        3

fruits = ['banana', 'apple', 'melon', 'pear']
first_fruit = fruits[0]
print('first fruit:', first_fruit)
second_fruit = fruits[1]
print('second fruit:', second_fruit)
third_fruit = fruits[2]
print(third_fruit)
# access the last fruit
last_fruit = fruits[-1]
print('last fruit:', last_fruit)

# Unpacking List Items of strings
_box = ['item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6', 'item_7']
a, b, c, *rest_of_items_in_box = _box     # unpacking the list into vairables (note: *rest_of_items_in_box grabs remainding items and stores into variable)
print('a:', a)
print('b:', b)
print('c:', c)
print('remainder:', rest_of_items_in_box)

# Unpack List items of integers
first, second, third, *rest, last = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(last)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing Items From a List
#
# Positive Indexing: We can specify a range of positive indexes by specifying the start, end, and step,
# the return value will be a new list
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
print(all_fruits)

# Negative indexing: We can specify a range of negative indexes by specifying the start, end, and step,
# the return value will be a new list
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-1]          # lemon
print(all_fruits)
all_fruits = fruits[-4]          # returns all fruits
orange_mango = fruits[-3:-1] # returns orange and mango without last index 
orange_mango_lemon = fruits[-3:] # returns orange and mango without last index
reverse_fruits = fruits[::-1]
print(all_fruits)
print(orange_mango)
print(orange_mango_lemon)
print(reverse_fruits)

# Modifying Lists
#
# List is a mutable or modifiable order collection of items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       # ['avocado', 'orange', 'mango', 'lemon' ]

fruits[1] = 'apple'
print(fruits)       # ['avocado', 'apple', 'mango', 'lemon' ]

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)       # ['avocado', 'apple', 'mango', 'lime' ]

# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits     # boolean variable that will check if 'banana' is found in fruits, will return True
print(does_exist)

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'lemon' in fruits     # boolean variable that will check if 'banana' is found in fruits, will return True
print(does_exist)

does_exist = 'lime' in fruits     # boolean variable that will check if 'banana' is found in fruits, will return False
print(does_exist)

# Adding Items to a List
#
# To add idem to the end of an existing list we use the method .append()
item = 'something'
_list = list()
_list.append(item)   # appending 'something' to our list
print(_list)         # will have 'something' inside

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)

fruits.append('lime')
print(fruits)

# Inserting Items Into a List
#
# Use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right
_item = 'another_item'
_index = 0
_list = ['item_1', 'item_2']
_list.insert(_index, _item)  # ['another_item', 'item_1', 'item_2']
print(_list)

_index = 1
_list = ['item_1', 'item_2']
_list.insert(_index, _item)  # ['item_1', 'another_item', 'item_2']
print(_list)

_index = 2
_list = ['item_1', 'item_2']
_list.insert(_index, _item)  # ['item_1', 'item_2', 'another_item']
print(_list)

# Removing Items From a List

# The remove method .remove() removes a specified item from a list