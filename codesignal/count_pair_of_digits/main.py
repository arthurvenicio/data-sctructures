def solution(n):
    counter = 0
    prev_digit = -1
    
    while n > 0:
        digit = n % 10
        
        if digit == prev_digit:
            counter += 1
        
        prev_digit = digit
        n //= 10
        
    return counter

print(solution(113224)) # 2