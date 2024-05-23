class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        nums.sort()
        # subtract 1 to exclude empty set
        return self.calc(nums, k, freq, 0) - 1

    def calc(self, nums: List[int], k: int, freq: defaultdict[int], i: int) -> int:
        if i == len(nums):
            return 1

        # calc num b subsets without nums[i]
        withoutElement = self.calc(nums, k, freq, i + 1)

        # calc num b subsets with nums[i]
        withElement = 0
        # check beautiful condition
        if freq[nums[i] - k] == 0:
            # take element
            freq[nums[i]] += 1
            withElement = self.calc(nums, k, freq, i + 1)
            # backtrack
            freq[nums[i]] -= 1

        return withoutElement + withElement
