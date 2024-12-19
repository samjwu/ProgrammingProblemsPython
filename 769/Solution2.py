class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        
        stk = []
        
        for i in range(n):
            # new chunk
            if not stk or arr[i] > stk[-1]:
                stk.append(arr[i])
            else:
                # add current val to prev chunk
                hi = stk[-1]
                
                while stk and arr[i] < stk[-1]:
                    stk.pop()
                    
                stk.append(hi)
        
        return len(stk)
