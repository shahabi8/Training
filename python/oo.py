class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __lt__(self, other):
        # check if other is not the linkList type
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) < len(other)

    def __le__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) <= len(other)

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) == len(other)

    def __ne__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) != len(other)

    def __gt__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) > len(other)

    def __ge__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) >= len(other)
    # str is used to printout linklist
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

# Example usage
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)

ll2 = LinkedList()
ll2.append(4)
ll2.append(5)

ll3 = LinkedList()
ll3.append(6)
ll3.append(7)
ll3.append(8)

print("LinkedList 1:", ll1)
print("LinkedList 2:", ll2)
print("LinkedList 3:", ll3)

print("LinkedList 1 < LinkedList 2:", ll1 < ll2)
print("LinkedList 1 <= LinkedList 2:", ll1 <= ll2)
print("LinkedList 1 == LinkedList 3:", ll1 == ll3)
print("LinkedList 1 != LinkedList 2:", ll1 != ll2)
print("LinkedList 1 > LinkedList 2:", ll1 > ll2)
print("LinkedList 1 >= LinkedList 3:", ll1 >= ll3)

# type conversion in python
class MyString:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def __repr__(self):
        return f'MyString({self.s!r})'

    def __int__(self):
        try:
            return int(self.s)
        except ValueError:
            raise ValueError(f"Cannot convert {self.s} to int")

    def __float__(self):
        try:
            return float(self.s)
        except ValueError:
            raise ValueError(f"Cannot convert {self.s} to float")

    def __bool__(self):
        return bool(self.s)

    def __bytes__(self):
        return bytes(self.s, 'utf-8')

    def to_list(self):
        return list(self.s)

# Example usage
my_str = MyString("123.45")

# String conversion
print(str(my_str))        # Output: 123.45
print(repr(my_str))       # Output: MyString('123.45')

# Integer conversion
try:
    print(int(my_str))    # Output: Raises ValueError
except ValueError as e:
    print(e)

# Float conversion
try:
    print(float(my_str))  # Output: 123.45
except ValueError as e:
    print(e)

# Boolean conversion
print(bool(my_str))       # Output: True

# Bytes conversion
print(bytes(my_str))      # Output: b'123.45'

# Custom list conversion
print(my_str.to_list())   # Output: ['1', '2', '3', '.', '4', '5']