class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def genSubsets(nums: List[int], index: int, subset: List[int], subsets: List[List[int]]) -> None:
            if index == len(nums):
                subsets.append(subset[:])
                return

            # generate subsets with nums[i]
            subset.append(nums[index])
            genSubsets(nums, index + 1, subset, subsets)

            # generate subsets without nums[i]
            subset.pop()
            genSubsets(nums, index + 1, subset, subsets)

        subsets = []
        genSubsets(nums, 0, [], subsets)
        ans = 0

        for subset in subsets:
            subsetXor = 0

            for num in subset:
                subsetXor ^= num

            ans += subsetXor

        return ans
