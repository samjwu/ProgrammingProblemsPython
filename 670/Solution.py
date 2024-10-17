class Solution:
    def maximumSwap(self, num: int) -> int:
        strs = list(str(num))

        n = len(strs)

        # swaps[i] = (inclusive) index of highest number to right of ith index
        swaps = [0 for i in range(n)]
        swaps[n-1] = n-1

        for i in range(n-2, -1, -1):
            if strs[i] > strs[swaps[i+1]]:
                swaps[i] = i
            else:
                swaps[i] = swaps[i+1]

        for i in range(n):
            if strs[i] < strs[swaps[i]]:
                strs[i], strs[swaps[i]] = strs[swaps[i]], strs[i]
                return int("".join(strs))

        return num
