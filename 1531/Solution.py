class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # return length of char repeated x times
        getLen = lambda x: x if x <= 1 else int(log10(x)) + 2
        
        @cache 
        def dp(i: int, k: int, prev: int, repeated: int) -> int:
            if k < 0:
                return inf

            if i == len(s): 
                return 0

            # remove current char
            ans = dp(i+1, k-1, prev, repeated)

            # try keeping current char
            if prev == s[i]:
                # need to account for increase in length of repeated
                repeatedChange = getLen(repeated+1) - getLen(repeated)
                ans = min(ans, dp(i+1, k, s[i], repeated+1) + repeatedChange)
            else:
                ans = min(ans, dp(i+1, k, s[i], 1) + 1)

            return ans 
        
        return dp(0, k, "", 0)
