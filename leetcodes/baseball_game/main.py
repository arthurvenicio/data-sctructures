from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for o in operations:
            if o == "C":
                stack.pop()
            elif o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(o))
                
        return sum(stack)
    
# Time complexity: O(n)
# Space complexity: O(n)