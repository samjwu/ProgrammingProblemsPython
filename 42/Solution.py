class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        ans = 0

        maxLeft = [0 for i in range(n)]
        maxRight = [0 for i in range(n)]

        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]
        
        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])
        
        for i in range(1, n-1):
            ans += min(maxLeft[i], maxRight[i]) - height[i]
        
        return ans
