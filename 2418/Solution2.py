class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDict = {}
        
        for name, height in zip(names, heights):
            heightDict[height] = name
            
        heights.sort(reverse=True)
        
        ans = []
        
        for height in heights:
            ans.append(heightDict[height])
            
        return ans
