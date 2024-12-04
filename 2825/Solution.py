class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def areCyclic(a: str, b: str) -> bool:
            return a == b or ord(a) + 1 == ord(b) or ord(a) - 25 == ord(b)

        n = len(str1)
        m = len(str2)

        j = 0
        
        for i in range(n):
            if j < m and areCyclic(str1[i], str2[j]):
                j += 1

        return j == m
