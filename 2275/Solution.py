class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bitFreq = [0] * 24

        # count bits of all numbers
        for i in range(24):
            for num in candidates:
                if (num & (1 << i)) != 0:
                    bitFreq[i] += 1

        return max(bitFreq)
