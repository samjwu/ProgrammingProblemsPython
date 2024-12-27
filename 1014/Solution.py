class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        n = len(values)
        bestPrev = (values[0], 0)
        
        for i in range(1, n):
            dist = bestPrev[1] - i
            currScore = bestPrev[0] + values[i] + dist
            ans = max(ans, currScore)
            
            effectivePrevValue = bestPrev[0] + dist
            effectiveCurrValue = values[i]
            if effectiveCurrValue > effectivePrevValue:
                bestPrev = (values[i], i)
        
        return ans
