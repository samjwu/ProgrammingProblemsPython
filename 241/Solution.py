class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        n = len(expression)

        # base case: empty expression
        if n == 0:
            return ans

        # base case: single number
        if n == 1:
            return [int(expression)]

        # base case: 2 digit number
        if n == 2 and expression[0].isdigit():
            return [int(expression)]

        # iterate and recurse
        for i, c in enumerate(expression):
            # skip processing digits
            if c.isdigit():
                continue

            # split expression into left and right
            left = self.diffWaysToCompute(expression[0:i])
            right = self.diffWaysToCompute(expression[i+1:n])

            # use op to combine left and right
            for l in left:
                for r in right:
                    if c == "+":
                        ans.append(l + r)
                    elif c == "-":
                        ans.append(l - r)
                    elif c == "*":
                        ans.append(l * r)

        return ans
