class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr = ""
        ans = []

        self.recurse(n, curr, ans)

        if len(ans) < k:
            return ""

        ans.sort()

        return ans[k - 1]

    def recurse(self, n: int, curr: str, ans: list):
        if len(curr) == n:
            ans.append(curr)
            return

        for c in "abc":
            # skip duplicate chars
            if len(curr) > 0 and curr[-1] == c:
                continue

            self.recurse(n, curr + c, ans)
