class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        freq = Counter([0])
        ans = 0
        prefix = 0

        for i in range(n):
            if nums[i] % modulo == k:
                prefix += 1
            
            ans += freq[(prefix - k + modulo) % modulo]
            freq[prefix % modulo] += 1

        return ans
