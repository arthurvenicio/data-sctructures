def repeat_char_jump(inputString, k):
    n = len(inputString)
    res = ''
    pointer = 0
    
    while len(res) < n:
        res += inputString[pointer]
        pointer = (pointer + k) % n
    return res


print(repeat_char_jump("abcdefg", 3))