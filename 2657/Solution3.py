class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        inserted = set()

        ans = []

        for i in range(n):
            inserted.add(A[i])
            inserted.add(B[i])

            ans.append(2 * (i+1) - len(inserted))

        return ans
