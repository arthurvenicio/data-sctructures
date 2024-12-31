from math import ceil, floor
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(int(b) + int(a))
                elif token == "-":
                    stack.append(int(b) - int(a))
                elif token == "*":
                    stack.append(int(b) * int(a))
                else:
                    division = int(b) / int(a)
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(floor(division))
            else:
                stack.append(int(token))

        return stack[-1]
    
    
# Time complexity: O(n)
# Space complexity: O(n)