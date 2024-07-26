from collections import defaultdict
from collections import OrderedDict
from collections import deque
import heapq
import sys
import random
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

# get last item and rest from list
path_vec = ['a','b','c']
 *dirs, last_item = path_vec

# copy one list to another
balance = ['1','2','3']
self.balance = balance[:]

# create list of keys from dic
dirs = defaultdict()
files = defaultdict()
output = list(files) + list(dirs)

#Iterating Through Keys:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# for loop over dic is going to give use keys
# for values you should do my_dict[key]
for key in my_dict:
    print(key)

#Iterating Through Values:

for value in my_dict.values():
    print(value)

#Iterating Through Key-Value Pairs:

for key, value in my_dict.items():
    print(key, value)

# get the only element in dictionary
(key, value) = list(my_dict.items())[0]

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

# dic of dic of string
defaultdict(lambda: defaultdict(str))

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

my_list = [4, 2, 9, 1, 5, 6]

# Sort the list in descending order
my_list.sort(reverse=True)
# or use -x in lambda
my_list.sort(key=lambda x: -x)

sorted_list = sorted(my_list, reverse=True)

# Example list of tuples
my_list = [(1, 2), (3, 1), (5, 6), (4, 3)]

# Sort the list of tuples based on the second element in descending order
my_list.sort(key=lambda x: x[1], reverse=True)
# -x
my_list.sort(key=lambda x: -x[1])
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)

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

# sort string with sorted
original_string = "amazon"
sorted_characters = sorted(original_string)
sorted_string = ''.join(sorted_characters)

# in this function we can use tuple to convert sorted list of char
# to tuple and use it as key in dic and also we can 
# return data.values() and it will implicitly get converted 
# to list(data.values())
def func():
    data = defaultdict(list)
    output, tp = [], []
    for s in strs:
        new_s = tuple(sorted(s))
        data[new_s].append(s)
    return data.values()

# compare strings lexicographically
str1 = "apple"
str2 = "banana"

if str1 < str2:
    print(f"{str1} is lexicographically smaller than {str2}")
elif str1 > str2:
    print(f"{str1} is lexicographically greater than {str2}")
else:
    print(f"{str1} is equal to {str2}")

# compare two lists lexicographically
def is_lexicographically_smaller(list1, list2):
    return list1 < list2

# Example usage
list1 = ["apple", "banana", "cherry"]
list2 = ["apple", "banana", "date"]

result = is_lexicographically_smaller(list1, list2)



id = s.find('/', starting_index)
# '/' not found returns -1
# better to use sting.split('/) if you want to
# to process string based on a delimiter

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

# min heap by default
x = [5, 7, 9, 1, 3]
heapq.heapify(x)

heap = []
heapq.heappush(heap, 3)
smallest = heapq.heappushpop(heap, 6)

smallest = heapq.heapreplace(heap, 2)
largest = heapq.nlargest(3, [1, 2, 3, 4, 5])
smallest = heapq.nsmallest(3, [1, 2, 3, 4, 5])

data = [5, 7, 9, 1, 3]
max_heap = [-x for x in data]
heapq.heapify(max_heap)

# Get the top (smallest/largest) element of the heap
top_element = max_heap[0]


# static class methods in python
class MyClass:
    static_member = 42

    @classmethod
    def static_method(cls):
        print("Static member:", cls.static_member)

# access static and non static attributes in python
class MyClass:
    # Static member
    static_member = "I am a static member"

    def __init__(self, value):
        self.instance_member = value

    @classmethod
    def modify_static_member(cls, new_value):
        cls.static_member = new_value

    def display(self):
        # Accessing static member using cls
        print("Static Member:", MyClass.static_member)
        print("Instance Member:", self.instance_member)

# private attributes in python
class MyClass:
    def __init__(self, value):
        self._weak_private_attribute = value
        self.__strong_private_attribute = value

    def get_private_attribute(self):
        return (self._private_attribute, self.__private_attribute)
    
# max of list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_number = max(numbers)
max_index = numbers.index(max_number)

max_index, max_number = max(enumerate(numbers), key=lambda x: x[1])
# enumerate creats list of tuples of (index, item)
# [(index1, item1), (index2, item2), ...]

# max int in pythons
max_int = sys.maxsize
float('inf')

#deque
d = deque([1, 2, 3, 4, 5])
d.append(6)
print(d)  # deque([1, 2, 3, 4, 5, 6])

# Append to the left
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4, 5, 6])

# Pop from the right
d.pop()
print(d)  # deque([0, 1, 2, 3, 4, 5])

# Pop from the left
d.popleft()
print(d)  # deque([1, 2, 3, 4, 5])

# Extend on the right
d.extend([6, 7])
print(d)  # deque([1, 2, 3, 4, 5, 6, 7])

# Extend on the left
d.extendleft([-1, -2])
print(d)  # deque([-2, -1, 1, 2, 3, 4, 5, 6, 7])

# Rotate the deque
d.rotate(2)
print(d)  # deque([6, 7, -2, -1, 1, 2, 3, 4, 5])

# Clear the deque
d.clear()
print(d)  # deque([])

# Copy the deque
d = deque([1, 2, 3])
d2 = d.copy()

from sortedcontainers import SortedDict, SortedList
sd = SortedDict()
sl = SortedList()
sd['apple'] = 5
sd['cherry'] = 2
sd.pop('cherry')
sl.add(10)
sl.add(5)
sl.remove(10)
for key, sl in sd.items():
    print(f"{key}: {list(sl)}")
# Custom key function to sort by the length of the string
sl = SortedList(key=len)
sl = SortedList(key=lambda x: len(x))
# no custom sorting for sortedDict

# defining global variable
cnt = 0
# Define the function that modifies the global variable
def match_orders(order, backlog, functor, order_backlog):
    global cnt
    # Example logic for the function
    cnt += 1

# Generate a random integer between 1 and 100 (inclusive)
random_number = random.randint(1, 100)
# floating point between 0 and 100 but not inclusive
random_number = 100 * random.random()