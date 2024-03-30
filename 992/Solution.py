class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)

    def subarraysWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        n = len(nums)

        ans  = 0

        left = 0

        for right in range(n):
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            ans  += right - left + 1

        return ans 
