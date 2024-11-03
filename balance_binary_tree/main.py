# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.deep_first_search(root)[0]
    
    def deep_first_search(self, node):
        if not node:
            return [True,0] # if node is null, already is balanced
        
        left = self.deep_first_search(node.left) # verify is the left side of the node is balanced
        right = self.deep_first_search(node.right)  # verify is the right side of the node is balanced
        
        is_balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) == 1
        
        return [is_balance, 1 + max(left[1], right[1])]          
            
        