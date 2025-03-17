class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        unpaired = defaultdict(bool)

        for num in nums:
            unpaired[num] = not unpaired[num]

        for key in unpaired:
            if unpaired[key] == True:
                return False

        return True
