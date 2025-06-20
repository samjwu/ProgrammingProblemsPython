class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        shortest_special = float('inf')

        for left in range(n):
            bitwise_or = 0

            for right in range(left, n):
                bitwise_or |= nums[right]

                if bitwise_or >= k:
                    shortest_special = min(shortest_special, right - left + 1)
                    break
        
        if shortest_special != float('inf'):
            return shortest_special
        return -1
