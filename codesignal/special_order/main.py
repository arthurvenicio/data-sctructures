def special_order(inputString):
    res = ''
    n = len(inputString)
    
    mid = n // 2 + n % 2
    
    for i in range(n):
        if i < mid:
            res += inputString[n - i - 1]
        else:
            res += inputString[i - mid]
           
    return res

print(special_order("abcdefg")) # gfedabc