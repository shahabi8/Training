# cycle detection in directed graph
# global visited to no visit healthy nodes again
# 
def dfs_cycle_detection(graph, node, visited, recStack):
    # Mark the current node as visited and add it to the recursion stack
    visited.add(node)
    recStack.add(node)
    
    # Recur for all neighbors
    for neighbor in graph[node]:
        # If the neighbor is not visited, recur on it
        if neighbor not in visited:
            if dfs_cycle_detection(graph, neighbor, visited, recStack):
                return True
        # If the neighbor is in the recursion stack, we found a cycle
        elif neighbor in recStack:
            return True
    
    # Remove the node from the recursion stack
    recStack.remove(node)
    return False

def has_cycle(graph):
    visited = set()
    recStack = set()
    
    # Check for cycles in different DFS trees
    for node in graph:
        if node not in visited:
            if dfs_cycle_detection(graph, node, visited, recStack):
                return True
    return False

# bfs and dfs to find connected parts of graph
# local visited to keep track of connections
def bfs(graph, node, visited):
    local_visited = set()  # To keep track of nodes visited in the current DFS run
    stack = [node]  # Stack for the iterative DFS
    
    while stack:
        current = stack.pop()  # Get the current node from the stack
        if current not in visited:
            visited.add(current)  # Mark the current node as globally visited
            local_visited.add(current)  # Mark the current node as locally visited
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)  # Add unvisited neighbors to the stack
    
    return local_visited  # Return all nodes visited in this DFS run

def dfs(graph, node, visited, local_visited):
    visited.add(node)
    local_visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, local_visited)

def find_all_components(graph):
    visited = set()  # To keep track of all globally visited nodes
    components = []  # To store all connected components
    
    for node in graph:
        if node not in visited:
            local_visited = set()
            dfs(graph, node, visited, local_visited)  # Perform DFS for unvisited nodes
            components.append(local_visited)  # Add the found component to the list
    
    return components  # Return all connected components

# cycle in undirected graph no need for local visited
# nodes that are connected through an edge can access each other
# whereas in directed grapg that's not the case
def dfs_cycle_detection(graph, node, visited, parent):
    visited.add(node)  # Mark the current node as visited
    
    for neighbor in graph[node]:  # Iterate over all neighbors
        if neighbor not in visited:
            # Recur for all unvisited neighbors
            if dfs_cycle_detection(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            # If an adjacent node is visited and not parent of current vertex, then there is a cycle
            return True
            
    return False

def has_cycle(graph):
    visited = set()  # Global set to keep track of visited nodes
    
    for node in graph:
        if node not in visited:
            # Call the recursive helper function to detect cycle in different DFS trees
            if dfs_cycle_detection(graph, node, visited, None):
                return True
                
    return False

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

# Example usage
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)
print(uf.connected(1, 3))  # Output: True
print(uf.connected(1, 4))  # Output: False

def kruskal(graph):
    # Step 1: Sort all edges in non-decreasing order of their weight
    edges = sorted(graph['edges'], key=lambda edge: edge[2])
    
    # Step 2: Initialize Union-Find structure
    uf = UnionFind(graph['vertices'])
    
    mst = []
    for edge in edges:
        u, v, weight = edge
        # Step 3: Check if the current edge forms a cycle
        if not uf.connected(u, v):
            uf.union(u, v)
            mst.append(edge)
    
    return mst

# Example usage
graph = {
    'vertices': 4,
    'edges': [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
}

# topology sort

from collections import deque, defaultdict

def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}  # Initialize in-degree of all vertices to 0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1  # Compute in-degree of each vertex

    queue = deque([u for u in graph if in_degree[u] == 0])  # Enqueue vertices with 0 in-degree
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1  # Decrease in-degree of neighbors
            if in_degree[v] == 0:
                queue.append(v)  # Enqueue vertices with 0 in-degree

    if len(topo_order) == len(graph):
        return topo_order
    else:
        return []  # Return empty list if there is a cycle (not a DAG)

# Example graph as adjacency list
graph = {
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

topo_sort = kahn_topological_sort(graph)
print("Topological Sort (Kahn's Algorithm):", topo_sort)

def dfs_topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    stack.reverse()  # Reverse the stack to get the topological order
    return stack


# backtracking pattern
# The key point in backtracking is that you are looking 
# for a solution by exploring various potential paths, 
# which means you need to "unvisit" nodes when you 
# backtrack to ensure they can be considered in different paths.
# Removing nodes would allow them to be reconsidered
def find_solution(candidate):
    pass

def is_valid(candidate):
    pass

def place(candidate):
    pass

def remove(candidate):
    pass

list_of_candidates = []
output = []
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)

# bfs word ladder problem
# below solutions show that for cases where size of words are lot smaller than number of words
# how we can improve complexity by reducing search space by generating generalized string mappings
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        # o(m2 * n) --> n words * m and *m for creating new string
        for word in wordList:
            for j in range(len(word)):
                adj[word[:j] + '*' + word[j + 1:]].append(word)

        def BFS(word, visited, dq):
            while len(dq) > 0:
                node, level = dq.popleft()
                visited.add(node)
                for i in range(len(node)):
                    pattern = node[:i] + '*' + node[i + 1:]
                    for word in adj[pattern]:
                        if word not in visited:
                            visited.add(word)
                            dq.append((word, level + 1))
                        if word == endWord:
                            return level + 1
            return 0

        dq = deque([(beginWord, 1)])
        visited = set([beginWord])
        return BFS(beginWord, visited, dq)
    
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff(s1, s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
                if cnt > 1:
                    break
            return cnt
        adj = defaultdict(list)
        # o (n ^ 2 * m) m to run diff
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if diff(wordList[i], wordList[j]) <= 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        if beginWord not in adj:
            for j in range(len(wordList)):
                if diff(beginWord, wordList[j]) <= 1:
                    adj[beginWord].append(wordList[j])
        def BFS(word, visited, dq):
            while len(dq) > 0:
                node, level = dq.popleft()
                visited.add(node)
                for i in adj[node]:
                    if i not in visited:
                        visited.add(node)
                        dq.append((i, level + 1))
                    if i == endWord:
                        return level + 1
            return 0

        dq = deque([(beginWord, 1)])
        visited = set([beginWord])
        return BFS(i, visited, dq)

# bi directional BFS
# first for this question we need to check if endWord is actually in wordList
# otherwise this approach may return wrong results
# The bfs need to be done for a queue that has smaller elements in it
# this is an optimazation, and in BFS we should have a for loop to run 
# over current number of element in queue, basically we need to run bfs level by level
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                adj[word[:j] + '*' + word[j + 1:]].append(word)
        if endWord not in wordList:
            return 0
        def BFS(dq, visited, visited_other):
            size = len(dq)
            for _ in range(size):
                node, level = dq.popleft()
                for i in range(len(node)):
                    pattern = node[:i] + '*' + node[i + 1:]
                    for word in adj[pattern]:
                        if word not in visited:
                            visited[word] = level + 1
                            dq.append((word, level + 1))
                        if word in visited_other:
                            return level + visited_other[word]
            return None 

        dqBegin = deque([(beginWord, 1)])
        dqEnd = deque([(endWord, 1)])
        visitedBegin = {beginWord: 1}
        visitedEnd = {endWord: 1}
        res = 0
        while dqBegin and dqEnd:
            if len(dqBegin) <= len(dqEnd):
                res = BFS(dqBegin, visitedBegin, visitedEnd)
            else:
                res = BFS(dqEnd, visitedEnd, visitedBegin)
            if res:
                return res
        return 0