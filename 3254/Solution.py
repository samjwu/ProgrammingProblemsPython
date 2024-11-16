class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        ans = [-1 for i in range(n-k+1)]

        # store indices in window
        window = collections.deque()

        for i in range(n):
            if window and window[0] < i-k+1:
                window.popleft()

            if window and nums[i] != nums[i-1] + 1:
                window.clear()

            window.append(i)

            if i >= k-1:
                if len(window) == k:
                    ans[i-k+1] = nums[window[-1]]
                else:
                    ans[i-k+1] = -1

        return ans
