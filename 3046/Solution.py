class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

            if freq[num] > 2:
                return False

        return True
