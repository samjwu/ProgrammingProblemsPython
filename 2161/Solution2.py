class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        less = 0
        equal = 0

        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1

        ans = [0] * n
        less_idx = 0
        equal_idx = less
        greater_idx = less + equal

        for num in nums:
            if num < pivot:
                ans[less_idx] = num
                less_idx += 1
            elif num > pivot:
                ans[greater_idx] = num
                greater_idx += 1
            else:
                ans[equal_idx] = num
                equal_idx += 1

        return ans
