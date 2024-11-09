"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> 'Optional[Node]':
        if not head:
            return None
        
        list_copy = {}
        
        current = head
        
        while current:
            list_copy[current] = Node(current.val)
            current = current.next
        
        current = head
        
        while current:
            list_copy[current].next = list_copy.get(current.next)
            list_copy[current].random = list_copy.get(current.random)
            current = current.next
            
        return list_copy
        
        
sol = Solution()

node1 = Node(2, None, 1)
head = Node(1, node1, 1)


sol.copyRandomList(head)
