class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        r = n-1
        
        # find longest non-decreasing subarray from [r, n-1]
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1

        ans = r
        l = 0

        # find longest non-decreasing subarray from [0, l]
        while l < r and (l == 0 or arr[l-1] <= arr[l]):
            while r < n and arr[l] > arr[r]:
                r += 1
            
            # find longest non-decreasing subarray with (l, r) removed
            ans = min(ans, r-l - 1)

            l += 1

        return ans
