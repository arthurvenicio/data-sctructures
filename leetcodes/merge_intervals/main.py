# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         ## should sort
#         intervals.sort(key = lambda i: i[0])
#         output = [intervals[0]]

#         for s, e in intervals:
#             last_end = output[-1][1]

#             if s <= last_end:
#                 output[-1][1] = max(last_end, e)
#             else:    
#                 output.append([s, e])

#         return output
    
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## should sort
        intervals.sort(key = lambda i: i[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged
    
# Time complexity: O(n log n)
# Space complexity: O(n)