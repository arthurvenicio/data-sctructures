from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        # Adjacency list with dictonarty - default
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited_set = set()
        visited_set.add(source)
        
        def dfs(node):
            if node == destination:
                return True
            
            for n_node in graph[node]:
                if n_node not in visited_set:
                    visited_set.add(n_node)
                    if dfs(n_node):
                        return True
                    
            return False
        
        return dfs(source)
    
sol = Solution()

print(sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))