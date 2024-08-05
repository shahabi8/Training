
from collections import deque
from collections import defaultdict
from collections import OrderedDict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def isPalindrome(head):
    fast = head
    slow = head
    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if top != slow.val:
            return False
        slow = slow.next

    return True

# in binary tree if we know the number of childs in the bottom layer (L)
# total number of nodes will be 2 * L - 1
# in full binary tree the max number of node in each layer is 2 ** n  where n starts from 0

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Function to convert a heapified array to a binary tree
def array_to_tree(heap):
    if not heap:
        return None

    # Create a list of tree nodes
    nodes = [TreeNode(value) for value in heap]

    # Link the nodes according to binary heap properties
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    # The root of the tree is the first element in the list
    return nodes[0]

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

heap = [1, 3, 6, 5, 9, 8]
root = array_to_tree(heap)

class Tree:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

def pack(tree):
    queue = []
    if not tree:
        return
    deq = deque([tree])
    while len(deq) > 0:
        tree = deq.popleft()
        if tree:
            queue.append(tree.val)
            deq.append(tree.left)
            deq.append(tree.right)
        else:
            queue.append(None)
    return queue

def unpack(queue):
    if len(queue) == 0:
        return
    root = Tree(queue[0])
    deq = deque([root])
    i = 1
    while i < len(queue):
        node = deq.popleft()
        if queue[i]:
            node.left = Tree(queue[i])
            deq.append(node.left)
        i += 1
        if i < len(queue) and queue[i]:
            node.right = Tree(queue[i])
            deq.append(node.right)
        i += 1
    return root

# trie implementation
class Trie:
    def __init__(self):
        self.data = {}
        self.end = False
    
class Prefix:
    def __init__(self):
        self.head = Trie()
        self.st = []
    
    def insert(self, payload):
        cur = self.head
        for ch in payload:
            if ch not in cur.data:
                cur.data[ch] = Trie()
            cur = cur.data[ch]
        cur.end = True
    
    def find_prefix_size(self):
        cur = self.head
        cnt = 0
        while cur and len(cur.data) == 1 and not cur.end:
            cur = list(cur.data.values())[0]
            cnt += 1
        return cnt



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        trie = Prefix()
        for st in strs:
            if len(st) == 0:
                return ''
            trie.insert(st)
        return strs[0][:trie.find_prefix_size()]
    
# linklist for LRU cache
# the trick for linklist is we defined two constant head and tail
# so this helps us eliminate tons of corner cases, no need to check whether 
# linklist is empty or not

class Node:
    def __init__(self, value = -1, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class linkList:

    def __init__(self):
        self.head = Node()
        self.last = Node()
        self.head.next = self.last
        self.last.prev = self.head
    
    def add(self, node):
        prev = self.last.prev
        prev.next = node
        node.prev = prev
        node.next = self.last
        self.last.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def move_to_right(self, node):
        self.remove(node)
        self.add(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.data = defaultdict(list)
        self.sz = capacity
        self.list = linkList()
        

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key][1]
            self.list.move_to_right(node)
            return self.data[key][0]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key][1]
            self.list.move_to_right(node)
            self.data[key][0] = value
            return
        node = Node(key)
        self.data[key] = [value, node]
        self.list.add(node)
        if len(self.data) > self.sz:
            node = self.list.head.next
            key = node.value
            del self.data[key]
            self.list.remove(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)
# another link list example where we initialize new_head with node and
# and return new_head.next. This way lots of corner cases are covered.
# Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head1 = list1
    head2 = list2
    new_head = ListNode(-1)
    cur = new_head
    while head1 and head2:
        if head1.val < head2.val:
            cur.next = head1
            head1 = head1.next
        else:
            cur.next = head2
            head2 = head2.next
        cur = cur.next
    if head1:
        cur.next = head1
    if head2:
        cur.next = head2
    return new_head.next

# log n update of prefix sum
# log n to calculate prefix sum
# array approach o(n) to update prefix sum
# and o(1) to calculate get prefix sum
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        # Insert leaf nodes in tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos, value):
        # Update the value at position pos
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, l, r):
        # Sum on interval [l, r)
        l += self.n
        r += self.n
        sum = 0
        while l < r:
            if l % 2:
                sum += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                sum += self.tree[r]
            l //= 2
            r //= 2
        return sum
