class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = 0
        right = -1
        freq = Counter()
        ans = 0

        for left in range(n):
            # expand window
            while pairs < k and right + 1 < n:
                right += 1
                pairs += freq[nums[right]]
                freq[nums[right]] += 1

            if pairs >= k:
                ans += n - right

            # shrink window
            freq[nums[left]] -= 1
            pairs -= freq[nums[left]]
            
        return ans
