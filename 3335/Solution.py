class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord("a")] += 1

        for i in range(t):
            freq2 = [0] * 26
            # z becomes ab
            freq2[0] = freq[25]
            freq2[1] = (freq[25] + freq[0]) % MOD

            # others are 1 letter changes
            for j in range(2, 26):
                freq2[j] = freq[j-1]

            freq = freq2

        ans = sum(freq) % MOD

        return ans
