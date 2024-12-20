from typing import Set


class Node:
    def __init__(self, val, neighborhood = []):
        self.val = val
        self.neighborhood = neighborhood


    # dfs uses stack to keep track of nodes
    def dfs(self, node):
        set = Set()
        
        def dfs_recursive(node):
            if node is None:
                return
            set.add(node.val)
            for neighbor in node.neighborhood:
                if neighbor.val not in set:
                    dfs_recursive(neighbor)
        return False
    
    # bfs uses queue to keep track of nodes
    def bfs(self, val):
        vistited_set = Set()
        return False 
        
        
root = Node(0)
a = Node(1)
b = Node(2)