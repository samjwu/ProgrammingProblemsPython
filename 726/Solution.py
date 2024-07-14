class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        # track parenthesis pairs with stack
        stk = [defaultdict(int)]

        idx = 0

        while idx < n:
            if formula[idx] == "(":
                stk.append(defaultdict(int))
                idx += 1

            elif formula[idx] == ")":
                currGroup = stk.pop()
                idx += 1

                # get subscript number
                number = ""
                while idx < n and formula[idx].isdigit():
                    number += formula[idx]
                    idx += 1

                if number:
                    number = int(number)
                    for atom in currGroup:
                        currGroup[atom] *= number

                for atom in currGroup:
                    stk[-1][atom] += currGroup[atom]

            else:
                atom = formula[idx]
                idx += 1

                # get extra lowercase atom letters
                while idx < n and formula[idx].islower():
                    atom += formula[idx]
                    idx += 1

                # get subscript number
                number = ""
                while idx < n and formula[idx].isdigit():
                    number += formula[idx]
                    idx += 1

                # no subscript number means 1 atom
                if number == "":
                    stk[-1][atom] += 1
                else:
                    stk[-1][atom] += int(number)

        sortedAtoms = dict(sorted(stk[0].items()))

        ans = ""
        for atom in sortedAtoms:
            # add atom letters
            ans += atom

            # add atom number
            if sortedAtoms[atom] > 1:
                ans += str(sortedAtoms[atom])

        return ans
