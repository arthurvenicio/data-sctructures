def solution(numbers):
    res = []
    l, r = 0,  len(numbers) - 1
    
    while l <= r: 
        res.append(numbers[l] + numbers[r])
        r -= 1
        l += 1
        
    return res

print(solution([1, 2, 3, 4, 5]))

# Time complexity: O(n)
# Space complexity: O(1)