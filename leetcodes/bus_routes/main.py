from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)
        queue = deque()
        queue.append((source, 0))
        
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
                
                
        visited_stop = set()
        visited_bus = set()
        
        while queue:
            stop, route_len = queue.popleft()
            
            if stop == target:
                return route_len
            
            for bus in graph[stop]:
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    
                    for stop in routes[bus]:
                        if stop not in visited_stop:
                            visited_stop.add(stop)
                            queue.append((stop, route_len + 1))
        
        return -1
    
# Time complexity: O(n²)
# Space complexity: O(n²)