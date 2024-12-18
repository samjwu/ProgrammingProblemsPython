class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        
        stk = []
        
        n = len(prices)
        
        for i in range(n-1, -1, -1):
            while stk and stk[-1] > prices[i]:
                stk.pop()
                
            if stk and stk[-1] <= prices[i]:
                ans.append(prices[i] - stk[-1])
            else:
                ans.append(prices[i])
                
            stk.append(prices[i])
                
        ans.reverse()
        
        return ans
