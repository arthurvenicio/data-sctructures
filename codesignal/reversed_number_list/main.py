def solution(numbers):
    res = []
    numbers_set = set(numbers)
    
    for num in numbers:
        reversed_num = int(str(num)[::-1])
        
        if reversed_num in numbers_set:
            res.append((num, reversed_num))
    
    return res

# Time complexity: O(n)
# Space complexity: O(n)