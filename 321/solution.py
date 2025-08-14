from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max_subsequence(nums: int, k: int) -> List[int]:
            # construct a monotonic decreasing stack
            # final merged will have the lexicographically largest number
            stack = []
            # number of elements to discard from nums
            discard = len(nums) - k

            for num in nums:
                # pop numbers smaller than current one
                while discard and stack and stack[-1] < num:
                    stack.pop()
                    discard -= 1
                stack.append(num)
            
            # if k is smaller than stack, return first k elements from stack
            return stack[:k]

        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            # merge the two lists into one number
            merged = []
            
            while nums1 or nums2:
                # take whichever is larger
                # or whichever remains
                # for ties take the lexicographically bigger remainder
                if nums1 > nums2:
                    merged.append(nums1.pop(0))
                else:
                    merged.append(nums2.pop(0))

            return merged

        max_number = []
        # try all possible ways to partition both lists
        # account for if nums2 is shorter than k
        start = max(0, k - len(nums2))
        # account for if nums1 is longer than k
        end = min(k, len(nums1)) + 1
        
        for i in range(start, end):
            # take i elements from nums1
            part1 = pick_max_subsequence(nums1, i)
            # take remaining elements from nums2 (k-i)
            part2 = pick_max_subsequence(nums2, k-i)
            
            candidate = merge(part1, part2)
            max_number = max(max_number, candidate)

        return max_number
