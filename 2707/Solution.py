class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        wordset = set(dictionary)
        memo = [51 for i in range(n)]
        
        def recurse(idx: int) -> int:
            if idx == n:
                return 0

            if memo[idx] != 51:
                return memo[idx]

            # try curr char as extra
            ans = recurse(idx + 1) + 1

            # try all possible splits
            for j in range(idx, n):
                curr = s[idx:j+1]

                # and check if they are in the dictionary
                if curr in wordset:
                    ans = min(ans, recurse(j + 1))

            memo[idx] = ans
            return memo[idx]
            
        return recurse(0)
