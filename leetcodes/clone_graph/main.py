"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = deque([node])

        clones = {}
        clones[node.val] = Node(node.val, [])

        while queue:
            curr = queue.popleft()
            curr_clone = clones[curr.val]

            for n in curr.neighbors:
                if n.val not in clones:
                    clones[n.val] = Node(n.val, [])
                    queue.append(n)

                curr_clone.neighbors.append(clones[n.val])

        return clones[node.val]
        