class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # start at 1 (1-indexed)
        ans = 1
        k -= 1

        while k > 0:
            diff = self.lexDiff(n, ans, ans + 1)

            # if curr lex diff is not hit within k steps, skip current number
            if diff <= k:
                # increment answer by 1, but decrement k by lex diff
                ans += 1
                k -= diff
            else: # curr lex diff is hit within k step, so proceed 1 step at a time
                # increase answer by appending 0, but decrement k by 1
                ans *= 10
                k -= 1

        return ans

    def lexDiff(self, n: int, a: int, b: int):
        diff = 0
        
        # continue appending digits until hit or exceed max
        # since in lexicographical order 10 comes before 2
        while a <= n:
            # get count of numbers between b and a
            # use min of n+1 for boundary edge case
            # ie: where n itself needs to be included in diff
            diff += min(n + 1, b) - a

            # append 0 to try next level of numbers
            a *= 10
            b *= 10

        return diff
