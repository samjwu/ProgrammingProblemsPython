class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # one 1, two of all other numbers
        ans = [0 for _ in range(n*2 - 1)]

        seen = [False for _ in range(n+1)]

        self.recurse(0, ans, seen, n)

        return ans

    def recurse(self, cur, ans, seen, n):
        if cur == len(ans):
            return True

        # current index already has number, move to next one
        if ans[cur] != 0:
            return self.recurse(cur + 1, ans, seen, n)

        # try numbers from n to 1
        for num in range(n, 0, -1):
            # skip already used numbers
            if seen[num]:
                continue

            # place number
            seen[num] = True
            ans[cur] = num

            # since 1 only appears once, can place it anywhere
            if num == 1:
                if self.recurse(cur + 1, ans, seen, n):
                    return True

            # for any other number, try placing both positions at once
            elif cur + num < len(ans) and ans[cur + num] == 0:
                ans[cur + num] = num

                if self.recurse(cur + 1, ans, seen, n):
                    return True

                # backtrack - undo 2nd placement
                ans[cur + num] = 0

            # backtrack - undo 1st placement
            ans[cur] = 0
            seen[num] = False

        return False
