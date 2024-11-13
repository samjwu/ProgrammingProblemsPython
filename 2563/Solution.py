class Solution:
    def lowerBound(self, nums: List[int], l: int, r: int, target: int) -> int:
        n = 0

        while l <= r:
            m = l + ((r - l) // 2)
            
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1

        return l

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        ans = 0

        nums.sort()
        
        for i in range(n):            
            # num pairs with sum < lower
            # with nums[i] as an element
            lowerCount = self.lowerBound(nums, i+1, n-1, lower - nums[i])

            # num pairs with sum < upper + 1
            # with nums[i] as an element
            upperCount = self.lowerBound(nums, i+1, n-1, upper - nums[i] + 1)

            # diff of these two is num pairs with sum in range [lower, upper]
            # using diff also removes duplicate pairs
            ans += upperCount - lowerCount

        return ans
