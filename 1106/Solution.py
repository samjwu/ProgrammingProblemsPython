class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = deque()

        for c in expression:
            # reached end of subexpression
            if c == ")":
                values = []
                while stk[-1] != "(":
                    values.append(stk.pop())
                
                stk.pop() # remove (
                op = stk.pop()
                
                result = self.evalSubExpression(op, values)
                stk.append(result)
            elif c != ",": # inside subexpression
                stk.append(c)

        return stk[-1] == "t"

    def evalSubExpression(self, op: str, values: list[str]) -> str:
        if op == "!":
            if values[0] == "t":
                return "f"
            else:
                return "t"

        if op == "&":
            for value in values:
                if value == "f":
                    return "f"
            return "t"

        if op == "|":
            for value in values:
                if value == "t":
                    return "t"
            return "f"

        return ""
