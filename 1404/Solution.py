class Solution:
    def numSteps(self, s: str) -> int:
        def addOne(st: List[str]) -> None:
            n = len(st)
            
            st[n-1] = "0"
            
            for i in range(n-2, -1, -1):
                if st[i] == "1":
                    st[i] = "0"
                else:
                    st[i] = "1"
                    return
            
            st.insert(0, "1")
            
        ans = 0
        st = [c for c in s]
        
        while len(st) > 1:
            ans += 1
            
            if st[-1] == "0":
                st.pop()
            else:
                addOne(st)
        
        return ans
