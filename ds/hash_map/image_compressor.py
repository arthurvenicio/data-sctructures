class ImageCompressor:
    def __init__(self):
        pass
    
    
    def compress(self, str):
        string_iter = list(str)
        left = 0
        right = 0
        
        final_srt = ""
        counter = 0
        while right < len(string_iter):
            
            if string_iter[left] == string_iter[right]:
                counter += 1
            else:
                final_srt += f'{string_iter[left]}{counter}'
                left = right
                counter = 1
            right += 1
        
            
        return final_srt + f'{string_iter[-1]}{counter}'
    
    def decompress(self, srt):
        left, right = 0, 1
        srt_list = list(srt)
        
        
        final_srt = ""
        while right < len(srt_list):
            for n in range(int(srt_list[right])):
                final_srt += srt_list[left]

            right += 2
            left += 2
        return final_srt
    
    
image_optimization = ImageOptimization()
string = "aaaaabbbbccccac"
str_encoded = image_optimization.encode(string)
str_decoded = image_optimization.decode(str_encoded)
print(str_encoded)
print(str_decoded)
print(str_decoded == string)