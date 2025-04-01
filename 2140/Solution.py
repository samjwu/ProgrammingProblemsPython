class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def recurse(i):
            if i >= len(questions):
                return 0

            points, jump = questions[i][0], questions[i][1]

            return max(recurse(i+1), points + recurse(i+1 + jump))

        return recurse(0)
