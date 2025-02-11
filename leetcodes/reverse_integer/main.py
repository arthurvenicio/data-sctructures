class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x *= sign

        while x:
            res = res * 10 + x % 10
            x //= 10

        if res < -2**31 or res > 2**31:
            return 0

        return sign * res

# Time complexity: O(log x)
# Space complexity: O(n)