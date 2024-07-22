class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDict = {}
        
        n = len(names)
        
        for i in range(n):
            heightDict[heights[i]] = names[i]
            
        heights.sort(reverse=True)
        
        ans = []
        
        for height in heights:
            ans.append(heightDict[height])
            
        return ans
