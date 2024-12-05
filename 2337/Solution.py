class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # store (char, index)
        startChars = []
        targetChars = []

        # store (non-underscore chars, index)
        for i in range(len(start)):
            if start[i] != "_":
                startChars.append((start[i], i))

            if target[i] != "_":
                targetChars.append((target[i], i))

        # number of chars must match
        if len(startChars) != len(targetChars):
            return False

        while not len(startChars) == 0:
            startChar, startIdx = startChars.pop(0)
            targetChar, targetIdx = targetChars.pop(0)

            # chars must match
            # for L, start char must be to right of target char
            # for R, start char must be to left of target char
            # (or in same position)
            if (startChar != targetChar
                or (startChar == "L" and startIdx < targetIdx)
                or (startChar == "R" and startIdx > targetIdx)
            ):
                return False

        return True
