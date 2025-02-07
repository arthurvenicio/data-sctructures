def solution(n):
    digit_sum = 0
    
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            if digit_sum == 0:
                digit_sum = 1
            digit_sum *= digit
            
        n = n // 10
    return digit_sum

print(solution(43172)) # 21

# Time complexity: O(n)
# Space complexity: O(1)
