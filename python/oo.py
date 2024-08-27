from collections import defaultdict, OrderedDict
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

# design
# define data type table so that it can carry all related data about the table
class table:
    def __init__(self, columns, name):
        self.name = name
        self.columns = columns
        self.rows = defaultdict(list)
        self.rowId = 1

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for i in range(len(names)):
            self.tables[names[i]] = table(columns[i], names[i])

    def insertRow(self, name: str, row: List[str]) -> None:
        if name not in self.tables or len(row) > self.tables[name].columns:
            return
        rowId = self.tables[name].rowId
        self.tables[name].rows[rowId].extend(row)
        self.tables[name].rowId += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return
        if rowId not in self.tables[name].rows:
            return
        del self.tables[name].rows[rowId]
        return

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name].rows \
           or columnId > self.tables[name].columns:
            return
        return self.tables[name].rows[rowId][columnId - 1]
    
# another design would be to use a very complex data structure to handle this problem
# in this case the data structure is two nested dictionary and one list inside the dictionary
# also it has difficulty deleting elements because of list, Instead of list it needs another
# dictionary and also a add some other data to carry what was the last row id
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = defaultdict(OrderedDict)
        n = len(names)
        for i in range(n):
            for cnt in range(1, columns[i] + 1):
                self.tables[names[i]][cnt] = []

    def insertRow(self, name: str, row: List[str]) -> None:
        if name not in self.tables or len(row) > len(self.tables[name]):
            return
        i = 0
        for cols in self.tables[name]:
            self.tables[name][cols].append(row[i])
            i += 1
        return

    def deleteRow(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return
        for cols in self.tables[name]:
            self.tables[name][cols][rowId - 1] = -1
        return

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or columnId not in self.tables[name]:
            return
        return self.tables[name][columnId][rowId - 1]