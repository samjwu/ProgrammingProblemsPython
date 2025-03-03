class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        ans = [0] * n
        less_idx = 0
        equal = 0
        greater = []

        for num in nums:
            if num < pivot:
                ans[less_idx] = num
                less_idx += 1
            elif num == pivot:
                equal += 1
            else:
                greater.append(num)

        while equal > 0:
            ans[less_idx] = pivot
            less_idx += 1
            equal -= 1

        for great in greater:
            ans[less_idx] = great
            less_idx += 1

        return ans
