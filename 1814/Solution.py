class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        rearranged = []

        for i in range(n):
            rearranged.append(nums[i] - self.rev(nums[i]))
        
        freq = defaultdict(int)
        ans = 0
        MOD = 1e9 + 7

        for num in rearranged:
            ans = (ans + freq[num]) % MOD
            freq[num] += 1
        
        return int(ans)
    
    def rev(self, num: int) -> int:
        ans = 0

        while num:
            ans *= 10
            ans += num % 10
            num //= 10

        return ans
