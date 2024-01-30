class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stk.append(token)
            else:
                op2 = stk.pop()
                op1 = stk.pop()
                
                match token:
                    case "+":
                        stk.append(str(int(op1) + int(op2)))
                    case "-":
                        stk.append(str(int(op1) - int(op2)))
                    case "*":
                        stk.append(str(int(op1) * int(op2)))
                    case "/":
                        stk.append(str(int(int(op1) / int(op2))))
                        
        return int(stk.pop())
