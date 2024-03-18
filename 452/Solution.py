class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        
        sortedPoints = sorted(points, key=lambda x: x[0])
        
        ans = 1 
        
        currPoint = sortedPoints[0]
        
        for i in range(1, n):
            if sortedPoints[i][0] <= currPoint[1]:
                currPoint[1] = min(currPoint[1], sortedPoints[i][1])
            else:
                currPoint = sortedPoints[i]
                ans += 1
        
        return ans
