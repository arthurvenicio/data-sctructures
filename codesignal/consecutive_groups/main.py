def solution(s):
    res = []
    n = len(s)
    
    pointer = n - 1
    
    current_char = None
    current_lenght = 0
    
    while pointer >= 0:
        c = s[pointer]
        if c is current_char:
            current_lenght += 1
        else:
            if current_char is not None:
                res.append((current_char, current_lenght))
            current_char = c
            current_lenght = 1
        
        pointer -= 1
        
    if current_char is not None:
        res.append((current_char, current_lenght))
    
    return res

print(solution("aaabbcccdde")) # [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)]