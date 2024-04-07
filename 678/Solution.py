class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        memo = [[-1 for j in range(n)] for i in range(n)]
        
        return self.isValidString(0, 0, s, memo)

    def isValidString(self, index: int, numOpen: int, s: str, memo: List[List[int]]) -> bool:
        if index == len(s):
            return numOpen == 0

        if memo[index][numOpen] != -1:
            return memo[index][numOpen] == 1

        isValid = False
        
        # for *, try all possibilities
        if s[index] == '*':
            # try (
            isValid |= self.isValidString(index + 1, numOpen + 1, s, memo)

            # try )
            if numOpen > 0:
                isValid |= self.isValidString(index + 1, numOpen - 1, s, memo)

            # try empty string
            isValid |= self.isValidString(index + 1, numOpen, s, memo)
        else:
            if s[index] == '(':
                isValid = self.isValidString(index + 1, numOpen + 1, s, memo)
            elif numOpen > 0:
                isValid = self.isValidString(index + 1, numOpen - 1, s, memo)

        memo[index][numOpen] = 1 if isValid else 0

        return isValid
