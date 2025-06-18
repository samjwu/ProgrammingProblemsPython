class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        triplets = []

        # greedily take smallest triplets
        nums.sort()

        for i in range(0, n, 3):
            # no valid solution
            if nums[i+2] - nums[i] > k:
                return []

            triplets.append([nums[i], nums[i + 1], nums[i + 2]])

        return triplets
