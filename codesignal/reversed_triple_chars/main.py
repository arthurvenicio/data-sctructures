def reversed_triple_chars(s: str) -> str:
    res = ''
    n = len(s)
    
    for i in range(0, n - (n % 3), 3):
        chunk = s[i:i+3]
        res += chunk[::-1]
        
    if n % 3:
        res += s[-(n % 3):]
        
    return res

print(reversed_triple_chars("abcdef")) # cbafed

