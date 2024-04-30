class Solution(object):
    def wonderfulSubstrings(self, word: str) -> int:
        # freq[bitMask] = number of times bitMask appears
        freq = defaultdict(int)

        # empty bit mask occurs once
        freq[0] = 1

        bitMask = 0

        ans = 0

        for c in word:
            bit = ord(c) - ord("a")

            bitMask ^= (1 << bit)

            # if bit mask was seen before,
            # there is a valid answer
            # by XOR current substring with previous substring
            # equivalent to finding all evens
            # this can be done for every previous instance
            ans += freq[bitMask]
            freq[bitMask] += 1

            # since up to 1 odd is allowed
            # loop over each char and check if it's the only odd one
            for i in range(0, 10):
                ans += freq[bitMask ^ (1 << i)]

        return ans
