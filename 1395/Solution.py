class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        teams = 0

        # memo[i][j] = num teams up to ith soldier of size j
        memoAsc = [[-1 for j in range(4)] for i in range(n)]
        memoDesc = [[-1 for j in range(4)] for i in range(n)]

        for i in range(n):
            numAsc = self.recurseAsc(rating, i, 1, memoAsc)
            numDesc = self.recurseDesc(rating, i, 1, memoDesc)
            teams += numAsc + numDesc

        return teams

    def recurseAsc(self, rating: List[int], idx: int, teamSize: int, memoAsc: List[List[int]]) -> int:
        n = len(rating)

        if idx == n:
            return 0

        if teamSize == 3:
            return 1

        if memoAsc[idx][teamSize] != -1:
            return memoAsc[idx][teamSize]

        ans = 0

        for i in range(idx+1, n):
            if rating[i] > rating[idx]:
                ans += self.recurseAsc(rating, i, teamSize + 1, memoAsc)

        memoAsc[idx][teamSize] = ans
        return ans

    def recurseDesc(self, rating: List[int], idx: int, teamSize: int, memoDesc: List[List[int]]) -> int:
        n = len(rating)

        if idx == n:
            return 0

        if teamSize == 3:
            return 1

        if memoDesc[idx][teamSize] != -1:
            return memoDesc[idx][teamSize]

        ans = 0

        for i in range(idx+1, n):
            if rating[i] < rating[idx]:
                ans += self.recurseDesc(rating, i, teamSize + 1, memoDesc)

        memoDesc[idx][teamSize] = ans
        return ans
