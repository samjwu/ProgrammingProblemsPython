class Solution:
    def maxSumOfNodes(self, index: int, isEven: int, nums: List[int], k: int, memo: List[List[int]]) -> int:
        if index == len(nums):
            # XOR op must be done on even number of nodes
            # if num ops is not even, return min val to discard that path
            if isEven != 1:
                return -float("inf")
            else:
                return 0
        
        if memo[index][isEven] != -1:
            return memo[index][isEven]
        
        # check both paths: result of not doing and doing XOR op
        noXor = nums[index] + self.maxSumOfNodes(index + 1, isEven, nums, k, memo)
        yesXor = (nums[index] ^ k) + self.maxSumOfNodes(index + 1, isEven ^ 1, nums, k, memo)

        # memoize max of both paths
        memo[index][isEven] = max(yesXor, noXor)
        return memo[index][isEven]

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = [[-1 for j in range(2)] for i in range(len(nums))]
        
        return self.maxSumOfNodes(0, 1, nums, k, memo)
