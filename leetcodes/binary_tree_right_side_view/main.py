# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        # Queue to perform breadth-first search (BFS), starting with the root node
        queue = deque([root])
        
        while queue:
            # Variable to store the last node seen at the current level
            rightSide = None
            # Get the number of nodes in the current level
            queue_length = len(queue)
            
            # Iterate through all nodes in the current level
            for _ in range(queue_length):
                # Remove the oldest node from the queue
                node = queue.popleft()
                if node:
                    # Update the rightmost node at the current level
                    rightSide = node
                    # Add the left child of the current node to the queue (if it exists)
                    queue.append(node.left)
                    # Add the right child of the current node to the queue (if it exists)
                    queue.append(node.right)
                    
            # If a valid rightmost node was found, add its value to the result
            if rightSide:      
                res.append(rightSide.val)
        #Return the list of results
        return res
    
# Time Complexy: O(n)
# Space Complexy: O(h)
# Method used: BFS - Level Traversal
