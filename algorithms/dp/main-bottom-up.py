class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        table = [0] * (n + 1)
        
        table[0] = 0
        table[1] = 1

        for i in range(2, n+1):
            table[i] = table[i - 2] + table[i - 1]

        return table[n]
    
# Tabulation
# time complexity: O(n)