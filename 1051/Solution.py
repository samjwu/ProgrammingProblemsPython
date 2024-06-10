class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correctHeights = [height for height in heights]
        correctHeights.sort()
        
        n = len(heights)
        
        ans = 0
        
        for i in range(n):
            if correctHeights[i] != heights[i]:
                ans += 1
            
        return ans
