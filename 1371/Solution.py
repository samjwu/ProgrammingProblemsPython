class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)

        # prefix bitmask for XOR of chars
        xorPrefix = 0

        # give vowels unique nonzero values (powers of 2) for bitmask
        # all other chars receive value of 0 for bitmask
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16

        # store earliest index where each XOR bitmask value is seen
        # note highest XOR value is 11111 in binary = 31 in decimal
        xorIndices = [-1] * 32

        ans = 0
        
        for i in range(n):
            # calculate XOR prefix bitmask
            xorPrefix ^= characterMap[ord(s[i]) - ord("a")]
            
            # record index of new nonzero XOR prefix bitmask
            if xorIndices[xorPrefix] == -1 and xorPrefix != 0:
                xorIndices[xorPrefix] = i

            # candidate answer is length between current index and 
            # earliest index where current XOR prefix bitmask was seen
            ans = max(ans, i - xorIndices[xorPrefix])

        return ans
