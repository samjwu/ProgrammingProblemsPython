class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        out = defaultdict(int)
        
        for path in paths:
            cities.add(path[0])
            cities.add(path[1])
            
            out[path[0]] += 1
            
        for city in cities:
            if out[city] == 0:
                return city
            
        return ""
