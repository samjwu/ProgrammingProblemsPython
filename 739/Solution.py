class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        ans = [0 for i in range(n)]
        
        # store day and temp
        stk = []
        
        for i in range(n-1, -1, -1):
            while len(stk) > 0:
                if stk[-1][1] > temperatures[i]:
                    ans[i] = stk[-1][0] - i
                    break
                else:
                    stk.pop()
                    
            stk.append([i, temperatures[i]])
                    
        return ans
