
# the idea is to check string from right to left
# we have forbiddeb strings in trie or set
# let's say for string baaa we move to next index and adding c
# now for cbaaa we need to check c, cb, cba, cbaa, cbaaa
# that means we can pass string cbaaa to trie to check if any of the 
# above is in forbidden or loop through 
# for k in range(left, min(left + 10, right + 1)):
#    if word[left:k+1] in forbidden_set:
# 
class Node:
    def __init__(self):
        self.data = {}
        self.end = False
class Trie:
    def __init__(self):
        self.head = Node()
    
    def insert(self, s):
        cur = self.head
        for ch in s:
            if ch not in cur.data:
                cur.data[ch] = Node()
            cur = cur.data[ch]
        cur.end = True
    
    def search(self, s):
        cur = self.head
        for i in range(len(s)):
            if s[i] not in cur.data:
                return -1
            cur = cur.data[s[i]]
            if cur.end: return i
        return -1

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        left, mx = 0, 0
        trie = Trie()
        for i in forbidden:
            trie.insert(i)
        forbidden_set = set(forbidden)
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            res = trie.search(word[left: right + 1])
            if res != -1:
                right = left + res - 1
            mx = max(right - left + 1, mx)

        return mx

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        res = 0
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k+1] in forbidden_set:
                    right = k - 1
                    break
            res = max(res, right - left + 1)
        return res