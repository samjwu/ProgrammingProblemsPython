class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        
        n = len(points)
        
        for i in range(1, n):
            ans += self.calc_dist(points[i-1], points[i])
            
        return ans
    
    def calc_dist(self, p1: List[int], p2: List[int]) -> float:
        dx = abs(p1[0] - p2[0])
        dy = abs(p1[1] - p2[1])
        
        return max(dx, dy)
