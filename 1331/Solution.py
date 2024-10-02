class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = sorted(arr)
        
        ranks = {}
        
        rank = 0
        
        for num in copy:
            if num not in ranks:
                rank += 1
                
            ranks[num] = rank
        
        ans = []
        
        for num in arr:
            ans.append(ranks[num])
        
        return ans
