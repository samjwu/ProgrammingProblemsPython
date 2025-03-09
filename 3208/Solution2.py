class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        
        # number of alternating colors in current window
        window_size = 1
        prev = colors[0]

        for i in range(1, n):
            # check if color is not alternating
            if colors[i] == prev:
                # reset window
                window_size = 1
                prev = colors[i]
                continue

            # expand window
            window_size += 1

            # found valid answer
            if window_size >= k:
                ans += 1

            prev = colors[i]

        # circular traversal
        for i in range(k - 1):
            # check if color is not alternating
            if colors[i] == prev:
                # no valid window remaining
                break

            # expand window
            window_size += 1

            # found valid answer
            if window_size >= k:
                ans += 1

            prev = colors[i]

        return ans
