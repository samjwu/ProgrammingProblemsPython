class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_metal = -1
        last_paper = -1
        last_glass = -1
        
        metal_time = 0
        paper_time = 0
        glass_time = 0
        
        for i in range(len(garbage)):
            for c in garbage[i]:
                if c == "M":
                    last_metal = i
                    metal_time += 1
                if c == "P":
                    last_paper = i
                    paper_time += 1
                if c == "G":
                    last_glass = i
                    glass_time += 1
        
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
            
        if last_metal > 0:
            metal_time += travel[last_metal-1]
        if last_paper > 0:
            paper_time += travel[last_paper-1]
        if last_glass > 0:
            glass_time += travel[last_glass-1]
            
        return metal_time + paper_time + glass_time
