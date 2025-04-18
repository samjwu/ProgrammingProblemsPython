class Solution:
    def countAndSay(self, n: int) -> str:
        def formPairs(s):
            m = len(s)
            pairs = []
            i = 0

            while i < m:
                count = 1
                while i < m-1 and s[i] == s[i+1]:
                    count += 1
                    i += 1
                pairs.append([s[i], count])
                i += 1

            return pairs

        def say(pairs):
            strs = []

            for c, count in pairs:
                strs.append(str(count)+c)

            return "".join(strs)

        ans = "1"
        
        for i in range(1, n):
            pairs = formPairs(ans)
            ans = say(pairs)

        return ans
