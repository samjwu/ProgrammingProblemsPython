class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        
        n = len(colors)
        
        i = 0
        
        while i < n-1:
            if colors[i] == colors[i+1]:
                longest = max(neededTime[i], neededTime[i+1])
                total = neededTime[i] + neededTime[i+1]
                
                i += 1
                
                while i < n-1 and colors[i] == colors[i+1]:
                    longest = max(longest, neededTime[i+1])
                    total += neededTime[i+1]
                    
                    i += 1
                
                ans += total - longest
                
            i += 1
          
        return ans
