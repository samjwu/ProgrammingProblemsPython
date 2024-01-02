class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        n = len(nums)
        
        freq = [0 for i in range(n+1)]
        
        for num in nums:
            if freq[num] >= len(ans):
                ans.append([])
                
            ans[freq[num]].append(num)
            freq[num] += 1
        
        return ans
