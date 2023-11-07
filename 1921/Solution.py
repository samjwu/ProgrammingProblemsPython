class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        
        turns = []
        
        for i in range(n):
            turns.append(ceil(dist[i] / speed[i]))
            
        turns.sort()
        
        for i in range(n):
            if i >= turns[i]:
                return i
            
        return n
