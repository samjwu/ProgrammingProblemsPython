from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # latest index where the ith bit was set to 1
        latest_bit_index = [-1] * 31
        
        smallest_subarrays = [0] * n

        for left in range(n - 1, -1, -1):
            # track rightmost bit index
            right = left

            for bit_position in range(31):
                if (nums[left] & (1 << bit_position)) == 0:
                    if latest_bit_index[bit_position] != -1:
                        right = max(right, latest_bit_index[bit_position])
                else:
                    latest_bit_index[bit_position] = left
            
            smallest_subarrays[left] = right - left + 1

        return smallest_subarrays
