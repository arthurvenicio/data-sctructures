def solution(n):
    num = 0
    mut = 1
    
    while n > 0:
        digit = n % 10
        num += digit * mut
        mut = mut * 10
        num += digit * mut
        mut = mut * 10
        n //= 10
    return num

# Time complexity: O(n)
# Space complexity: O(1)