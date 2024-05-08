class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # map score to index
        idxMap = {}
        
        n = len(score)
        
        for i in range(n):
            idxMap[score[i]] = i
            
        score.sort(reverse=True)
        
        ans = [0 for i in range(n)]
        
        for i in range(n):
            if i == 0:
                ans[idxMap[score[i]]] = "Gold Medal"
            elif i == 1:
                ans[idxMap[score[i]]] = "Silver Medal"
            elif i == 2:
                ans[idxMap[score[i]]] = "Bronze Medal"
            else:
                ans[idxMap[score[i]]] = str(i+1)
        
        return ans
