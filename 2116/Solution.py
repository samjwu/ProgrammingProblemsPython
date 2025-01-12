class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n % 2 == 1:
            return False

        open = []
        unlocked = []

        for i in range(n):
            # treat unlocked as a wildcard
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(": # normal stack logic
                open.append(i)
            elif s[i] == ")":
                # greedily use existing open bracket (cheapest)
                # or use an unlocked wildcard
                # if neither available impossible to balance
                if open:
                    open.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # match up left over open with unlocked wildcard
        # wildcard must be after open bracket
        while open and unlocked and open[-1] < unlocked[-1]:
            open.pop()
            unlocked.pop()

        if open:
            return False

        return True
