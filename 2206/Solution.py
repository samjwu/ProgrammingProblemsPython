class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for key in freq:
            if freq[key] % 2 != 0:
                return False

        return True
