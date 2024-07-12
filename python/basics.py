from collections import defaultdict
from collections import OrderedDict
add = lambda x, y: x + y

# sort
points = [(2, 3), (4, 1), (5, 7), (1, 2)]
points_sorted = sorted(points, key=lambda point: point[1])

# Function pass to function
def apply_function(x, func):
    return func(x)

result = apply_function(5, lambda x: x * x)

numbers = [1, 2, 3, 4, 5]

# Equivalent of map to square the numbers
squared = [x ** 2 for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]

# Equivalent of filter to get even numbers
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4]

# Combining both operations
squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
print(squared_evens)  # Output: [4, 16]

tuple(['cat', 'dog', 5])
# ('cat', 'dog', 5)

list(('cat', 'dog', 5))
# ['cat', 'dog', 5]

list('hello')
# ['h', 'e', 'l', 'l', 'o']

#Iterating Through Keys:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key in my_dict:
    print(key)

#Iterating Through Values:

for value in my_dict.values():
    print(value)

#Iterating Through Key-Value Pairs:

for key, value in my_dict.items():
    print(key, value)

# keys(): Returns a view object containing the keys of the dictionary.

keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])

# values(): Returns a view object containing the values of the dictionary.
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 31])

#items(): Returns a view object containing the key-value pairs of the dictionary.
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 31)])

#update(): Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
my_dict.update({"city": "Los Angeles", "age": 32})
print(my_dict)  # Output: {'name': 'Alice', 'age': 32, 'city': 'Los Angeles'}

#popitem(): Removes and returns the last key-value pair added to the dictionary.
last_item = my_dict.popitem()
print(last_item)  # Output: ('city', 'Los Angeles')

#setdefault(): Returns the value of a key if it is in the dictionary. If not, it inserts the key with a specified value.
age = my_dict.setdefault("age", 25)
print(age)  # Output: 32 (since 'age' is already in the dictionary)
favorite_color = my_dict.setdefault("favorite_color", "blue")
print(favorite_color) 


# Example list
my_list = [1, 2, 3, 2]

# append
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 2, 4]

# extend
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 2, 4, 5, 6]

# insert
my_list.insert(2, 'a')
print(my_list)  # Output: [1, 2, 'a', 3, 2, 4, 5, 6]

# remove
my_list.remove(2)
print(my_list)  # Output: [1, 'a', 3, 2, 4, 5, 6]

# pop
item = my_list.pop(1)
print(item)  # Output: 'a'
print(my_list)  # Output: [1, 3, 2, 4, 5, 6]

# clear
my_list.clear()
print(my_list)  # Output: []

# reset the list
my_list = [1, 2, 3, 2]

# index
idx = my_list.index(2)
print(idx)  # Output: 1

# count
count = my_list.count(2)
print(count)  # Output: 2

# sort
my_list.sort()
print(my_list)  # Output: [1, 2, 2, 3]

my_list.sort(reverse=True)
print(my_list)  # Output: [3, 2, 1]

# reverse
my_list.reverse()
print(my_list)  # Output: [3, 2, 2, 1]

# copy
new_list = my_list.copy()
print(new_list)  # Output: [3, 2, 2, 1]

# Example set
my_set = {1, 2, 3}

# add
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# update
my_set.update([5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# remove
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

# discard
my_set.discard(3)
print(my_set)  # Output: {1, 4, 5, 6}

# pop
item = my_set.pop()
print(item)  # Output: 1 (or another item, as sets are unordered)
print(my_set)  # Output: {4, 5, 6}

# clear
my_set.clear()
print(my_set)  # Output: set()

# reset the set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# symmetric_difference
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# issubset
print(set1.issubset(set2))  # Output: False

# issuperset
print(set1.issuperset(set2))  # Output: False

# isdisjoint
print(set1.isdisjoint(set2))  # Output: False

# Example 1: Using int as the Default Factory
int_dict = defaultdict(int)
int_dict['a'] += 1
print("Example 1:", int_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})

# Example 2: Using list as the Default Factory
list_dict = defaultdict(list)
list_dict['a'].append(1)
print("Example 2:", list_dict)  # Output: defaultdict(<class 'list'>, {'a': [1]})

# Example 3: Using a Lambda Function as the Default Factory
lambda_dict = defaultdict(lambda: 10)
print("Example 3:", lambda_dict['a'])  # Output: 10
print(lambda_dict)

names = [("Alice", "Math"), ("Bob", "English"), ("Alice", "English"), ("Bob", "Math")]
group_dict = defaultdict(list)
for name, subject in names:
    group_dict[name].append(subject)

ordered_dict = OrderedDict()

# Adding elements
ordered_dict['apple'] = 3
ordered_dict['banana'] = 2
ordered_dict['orange'] = 5

# Accessing elements
print("Original OrderedDict:", ordered_dict)
# Output: OrderedDict([('apple', 3), ('banana', 2), ('orange', 5)])

# Inserting elements
ordered_dict['pear'] = 4
print("After inserting pear:", ordered_dict)
# Output: OrderedDict([('apple', 3), ('banana', 2), ('orange', 5), ('pear', 4)])

# Moving elements to the end
ordered_dict.move_to_end('banana')
print("After moving banana to the end:", ordered_dict)
# Output: OrderedDict([('apple', 3), ('orange', 5), ('pear', 4), ('banana', 2)])

# Moving elements to the beginning
ordered_dict.move_to_end('pear', last=False)
print("After moving pear to the beginning:", ordered_dict)
# Output: OrderedDict([('pear', 4), ('apple', 3), ('orange', 5), ('banana', 2)])

# Popping elements
popped_item = ordered_dict.popitem()
print("Popped item:", popped_item)
# Output: ('banana', 2)
print("After popping the last item:", ordered_dict)
# Output: OrderedDict([('pear', 4), ('apple', 3), ('orange', 5)])

popped_item_first = ordered_dict.popitem(last=False)
print("Popped first item:", popped_item_first)
# Output: ('pear', 4)
print("After popping the first item:", ordered_dict)
# Output: OrderedDict([('apple', 3), ('orange', 5)])

# Clearing the OrderedDict
ordered_dict.clear()
print("After clearing:", ordered_dict)
# Output: OrderedDict()

# Initializing with a list of tuples
list_of_tuples = [('apple', 3), ('banana', 2), ('orange', 5)]
ordered_dict1 = OrderedDict(list_of_tuples)
print("OrderedDict from list of tuples:", ordered_dict1)
# Output: OrderedDict([('apple', 3), ('banana', 2), ('orange', 5)])

# Initializing with a list of lists
list_of_lists = [['apple', 3], ['banana', 2], ['orange', 5]]
ordered_dict2 = OrderedDict(list_of_lists)
print("OrderedDict from list of lists:", ordered_dict2)
# Output: OrderedDict([('apple', 3), ('banana', 2), ('orange', 5)])

# Initializing with a tuple of tuples
tuple_of_tuples = (('apple', 3), ('banana', 2), ('orange', 5))
ordered_dict3 = OrderedDict(tuple_of_tuples)
print("OrderedDict from tuple of tuples:", ordered_dict3)
# Output: OrderedDict([('apple', 3), ('banana', 2), ('orange', 5)])

# Initializing with a dictionary (though order is not guaranteed in < Python 3.7)
regular_dict = {'apple': 3, 'banana': 2, 'orange': 5}
ordered_dict4 = OrderedDict(regular_dict.items())
print("OrderedDict from regular dictionary:", ordered_dict4)

items = [('apple', 3), ('banana', 2), ('orange', 5), ('pear', 4)]

# Sort items based on the second element (value)
sorted_items = sorted(items, key=lambda item: item[1])

# Create an OrderedDict from the sorted items
ordered_dict = OrderedDict(sorted_items)

s = "  Hello World  "

# Convert to lower case
print(s.lower())  # Output: "  hello world  "

# Convert to upper case
print(s.upper())  # Output: "  HELLO WORLD  "

# Convert to title case
print(s.title())  # Output: "  Hello World  "

# Swap case
print(s.swapcase())  # Output: "  hELLO wORLD  "

# Strip whitespace
print(s.strip())  # Output: "Hello World"

# Split into list
print(s.split())  # Output: ["Hello", "World"]

# Join list into string
words = ["Hello", "Python"]
print(" ".join(words))  # Output: "Hello Python"

', '.join(['cats', 'rats', 'bats'])
# 'cats, rats, bats'

# Find substring
print(s.find("World"))  # Output: 8

s = "hello world"
print(s.rfind("o"))  # Output: 7

# Count occurrences
print(s.count("l"))  # Output: 3

# Check if string starts with
print(s.startswith("  Hello"))  # Output: True

# Check if string ends with
print(s.endswith("World  "))  # Output: True

# Check if all characters are alphabetic
print("Hello".isalpha())  # Output: True

s = "hello123"
print(s.isalnum())  # Output: True

# Check if all characters are digits
print("12345".isdigit())  # Output: True

s = "hello"
print(s.islower())  # Output: True

s = "HELLO"
print(s.isupper())  # Output: True

s = "   "
print(s.isspace())  # Output: True

# Format string
print("Hello, {}!".format("world"))  # Output: "Hello, world!"

s = "42"
print(s.zfill(5))  # Output: "00042"

s = "hello"
print(s.ljust(10, '-'))  # Output: "hello-----"

s = "hello"
print(s.rjust(10, '-'))  # Output: "-----hello"