class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        
        idx = 0
        
        for i in range(1, n+1):
            if idx == len(target):
                break
                
            if i == target[idx]:
                ans.append("Push")
                idx += 1
            else: 
                ans.append("Push")
                ans.append("Pop")
                
        return ans
