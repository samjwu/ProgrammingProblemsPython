class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def generateSubsets(nums: List[int], index: int, currSubset: List[int], subsets: List[List[int]]) -> None:
            if index == len(nums):
                subsets.append(currSubset[:])
                return
            
            currSubset.append(nums[index])
            generateSubsets(nums, index + 1, currSubset, subsets)
            
            currSubset.pop()
            generateSubsets(nums, index + 1, currSubset, subsets)
            
        generateSubsets(nums, 0, [], ans)
        
        return ans
