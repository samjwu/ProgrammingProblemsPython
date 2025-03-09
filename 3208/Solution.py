class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # add the first k-1 colors to the end
        # to simplify circular traversal
        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)
        ans = 0

        # sliding window        
        left = 0
        right = 1

        while right < n:
            # check if color is not alternating
            if colors[right] == colors[right - 1]:
                # reset window
                left = right
                right += 1
                continue

            # expand window
            right += 1

            # do not increment answer until window size is valid
            if right - left < k:
                continue

            # found valid answer, slide the window
            ans += 1
            left += 1

        return ans
