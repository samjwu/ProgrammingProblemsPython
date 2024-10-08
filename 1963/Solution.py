class Solution:
    def minSwaps(self, s: str) -> int:
        stk = deque()
        
        extraClosing = 0
        
        for c in s:
            if c == '[':
                stk.append(c)
            else:
                if stk:
                    stk.pop()
                else:
                    extraClosing += 1
             
        # can fix max of 2 at a time
        return (extraClosing + 1) // 2
