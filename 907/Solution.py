class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1e9+ 7
        
        n = len(arr)
        
        stk = deque()
        
        ans = 0
        
        for i in range(n+1):
            # i == n means all elements were processed and stack should be cleared
            # arr[-1] >= arr[i] ensures that no contribution is counted twice
            while stk and (i == n or arr[stk[-1]] >= arr[i]):
                mid = stk.pop()
                
                # elements strictly less than arr[i]
                leftBound = -1 if not stk else stk[-1]
                
                # elements less than or equal to arr[i]
                rightBound = i
                
                # count = number of subarrays where mid is the minimum element
                count = (mid - leftBound) * (rightBound - mid) % MOD
                
                ans += (count * arr[mid]) % MOD
                ans %= MOD
                
            stk.append(i)
            
        return int(ans)
