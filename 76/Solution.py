class Solution:
    def minWindow(self, s: str, t: str) -> str:
        currFreq = Counter()
        targetFreq = Counter(t)

        l = 0
        r = 0

        n = len(s)

        candidates = []

        while r < n:
            # expand window until it contains target
            currFreq[s[r]] += 1
            r += 1

            if currFreq & targetFreq != targetFreq:
                continue

            # shrink window until it no longer contains target
            while l < r:
                currFreq[s[l]] -= 1
                l += 1

                if currFreq & targetFreq == targetFreq:
                    continue

                candidates.append(s[l - 1 : r])
                break

        if not candidates:
            return ""

        return min(candidates, key=len)
