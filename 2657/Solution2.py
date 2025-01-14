class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        freq = [0] * n

        ans = []
        common = 0

        for i in range(n):
            freq[A[i]-1] += 1
            if freq[A[i]-1] == 2:
                common += 1

            freq[B[i]-1] += 1
            if freq[B[i]-1] == 2:
                common += 1

            ans.append(common)

        return ans
