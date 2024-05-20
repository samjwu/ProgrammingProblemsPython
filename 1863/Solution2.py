class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def calculateXorValues(nums: List[int], index: int, xorValue: int) -> int:
            if index == len(nums):
                return xorValue
            
            withElement = calculateXorValues(nums, index + 1, xorValue ^ nums[index])
            withoutElement = calculateXorValues(nums, index + 1, xorValue)

            return withElement + withoutElement

        return calculateXorValues(nums, 0, 0)
