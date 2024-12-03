class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m = len(spaces)
        n = len(s)
        
        ans = []
        
        idx = 0
        
        for i in range(n):
            if idx < m and spaces[idx] == i:
                ans.append(' ')
                idx += 1

            ans.append(s[i])
        
        return "".join(ans)
