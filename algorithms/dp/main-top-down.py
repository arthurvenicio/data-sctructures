class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        hash = {0:0, 1:1}

        def fibo(num):
            if num in hash:
                return hash[num]
            
            hash[num] = fibo(num - 2) + fibo(num - 1)
            return hash[num]

        return fibo(n)