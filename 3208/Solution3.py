class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        
        # number of alternating colors in current window
        window_size = 1
        prev = colors[0]

        # circular traversal
        for i in range(1, n + k - 1):
            # use modulo for wrap-around
            index = i % n

            # check if color is not alternating
            if colors[index] == prev:
                # reset window
                window_size = 1
                prev = colors[index]
                continue

            # expand window
            window_size += 1

            # found valid answer
            if window_size >= k:
                ans += 1

            prev = colors[index]

        return ans
