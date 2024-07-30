class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        # prefixSumA[i] = number of A to the right of i
        prefixSumA = [0 for i in range(n)]
        countA = 0

        for i in range(n-1, -1, -1):
            prefixSumA[i] = countA
            if s[i] == "a":
                countA += 1

        # prefixSumB[i] = number of B to the left of i
        prefixSumB = [0 for i in range(n)]
        countB = 0

        for i in range(n):
            prefixSumB[i] = countB
            if s[i] == "b":
                countB += 1

        ans = n
        
        # at each index i, compute deletions of 
        # A to the right of i and 
        # B to the left of i
        for i in range(n):
            ans = min(ans, prefixSumA[i] + prefixSumB[i])

        return ans
