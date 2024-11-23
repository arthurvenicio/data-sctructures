class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}" :"{", "]": "["}

        for ch in s:
            if ch in mapping:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not len(stack)
        
        
sol = Solution()


print(sol.isValid("(]"))