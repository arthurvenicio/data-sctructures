from collections import deque
from typing import Set


class Node:
    def __init__(self, val, neighborhood = []):
        self.val = val
        self.neighborhood = neighborhood

class Graph:
    def __init__(self):
        pass
    
    # dfs uses call stack to keep track of nodes
    # time complexy: O(v + e)
    # space complexy: O(v + e)
    def dfs(self, node):
        seen_set = set()
        
        def dfs_recursive(node):
            if node is None:
                return
            
            print(node.val)
            seen_set.add(node.val)
            
            for neighbor in node.neighborhood:
                if neighbor.val not in seen_set:
                    dfs_recursive(neighbor)
        return dfs_recursive(node)
    
    # bfs uses queue to keep track of nodes
    # time complexy: O(v + e)
    # space complexy: O(v + e)
    def bfs(self, node):
        seen_set = set()
        queue = deque()
        
        queue.append(node)
        seen_set.add(node.val)
        
        while queue:
            node = queue.popleft()
            print(node.val)
            for neighbor in node.neighborhood:
                if neighbor.val not in seen_set:
                    seen_set.add(node.val)
                    queue.append(neighbor)
        

root = Node(0)
a = Node(1)
b = Node(2)
root.neighborhood = [a, b]

graph = Graph()
# graph.dfs(root)
graph.bfs(root)