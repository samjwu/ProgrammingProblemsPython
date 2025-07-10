class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        dupe_xor = 0

        for num in freq:
            if freq[num] == 2:
                dupe_xor ^= num

        return dupe_xor
