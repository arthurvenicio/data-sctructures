def encode_rle(s):
    res = ""
    current_char = None
    current_chat_lenght = 0
        
    for c in s:
        if c.isalnum():
            if c == current_char:
                current_chat_lenght += 1
            else:
                if current_char is not None:
                    res += f"{current_char}{current_chat_lenght}"
                current_char = c
                current_chat_lenght = 1
    if current_char is not None:
        res += f"{current_char}{current_chat_lenght}"
        
    return res

# Time complexity: O(n)
# Space complexity: O(1)