class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        
        num = 1
        
        for i in range(len(target)):
            while num != target[i]:
                ans.append("Push")
                ans.append("Pop")
                num += 1
                
            ans.append("Push")
            num += 1
                
        return ans
