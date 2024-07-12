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