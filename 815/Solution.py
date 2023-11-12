from queue import Queue

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        n = len(routes)
        
        graph = defaultdict(list)
        for route in range(n):
            for bus_stop in routes[route]:
                graph[bus_stop].append(route)
                
        q = Queue()
        seen = set()
        for route in graph[source]:
            q.put(route)
            seen.add(route)
            
        ans = 1
        while q.empty() is False:
            sz = q.qsize()
            
            for i in range(sz):
                route = q.get()
                
                for bus_stop in routes[route]:
                    if bus_stop == target:
                        return ans
                    
                    for next_route in graph[bus_stop]:
                        if next_route not in seen:
                            q.put(next_route)
                            seen.add(next_route)
                        
            ans += 1
        
        return -1
