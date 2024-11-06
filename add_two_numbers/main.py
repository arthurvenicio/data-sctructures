# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        
        dummy = ListNode()
        curr = dummy
        
        rest = 0

        while l1 is not None and l2 is not None or rest != 0:
            sum = rest
             
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
                
            rest = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
        return dummy.next
            
            
sol = Solution()

nodeA1= ListNode(3)
nodeA2= ListNode(4, nodeA1)
headA = ListNode(2, nodeA2)


nodeB1= ListNode(4)
nodeB2= ListNode(6, nodeB1)
headB = ListNode(5, nodeB2)


sol.addTwoNumbers(headA, headB)