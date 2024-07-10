class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        
        for l in logs:
            if l == "../":
                if len(stk) > 0:
                    stk.pop()
            elif l == "./":
                continue
            else:
                stk.append(l)
                
        return len(stk)
