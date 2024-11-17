class Solution:
    def merge_sort(self, arr):
        lenght = len(arr)
        
        if lenght == 1:
            return arr
        
        mid = lenght // 2
        
        arr_left = arr[:mid]
        arr_right = arr[mid:]
        
        arr_left = self.merge_sort(arr_left)
        arr_right  = self.merge_sort(arr_right)
        
        return self.merge(arr_left, arr_right)
    
    def merge(self, arrL, arrR):
        res = []
        i, j = 0, 0
        
        while i < len(arrL) and j < len(arrR):
            if arrL[i] < arrR[j]:
                res.append(arrL[i])
                i += 1
            else:
                res.append(arrR[j])
                j += 1
        
        res.extend(arrL[i:])
        res.extend(arrR[j:])      
        
        return res  
        
        
# Worst case, time complexy is O(n log n)


sol = Solution()


print(sol.merge_sort([2,8,6,3,7,9]))