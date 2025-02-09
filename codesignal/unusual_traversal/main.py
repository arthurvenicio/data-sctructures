def unusual_traversal(array):
    res = []
    n = len(array)
    
    mid = n // 2
    res.append(array[mid])
    
    left, right =  mid - 1, mid + 1
    
    while left >= 0 and right < n:
        if left >= 1:
            res.extend([array[left -1], array[left]])
            left -= 2
        elif left == 0:
            res.append(array[left])
            left -= 1
            
        if right < n - 1:
            res.extend([array[right], array[right + 1]])
            right += 2
        elif right == n - 1:
            res.append(array[right])
            right += 1
    
    return res

# Time complexity: O(n)
# Space complexity: O(n)

print(unusual_traversal([1, 2, 3, 4, 5, 6, 7])) # [4, 2, 3, 5, 6, 1, 7]