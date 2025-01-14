class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()

        n = len(A)

        ans = []

        for i in range(n):
            set_a.add(A[i])
            set_b.add(B[i])
            ans.append(len(set_a.intersection(set_b)))

        return ans
