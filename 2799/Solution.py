class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        window = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                window[remove] -= 1

                if window[remove] == 0:
                    window.pop(remove)

            while right < n and len(window) < distinct:
                add = nums[right]
                window[add] = window.get(add, 0) + 1
                right += 1

            if len(window) == distinct:
                ans += n - right + 1
                
        return ans
