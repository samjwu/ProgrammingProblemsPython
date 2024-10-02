class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = sorted(set(arr))
        
        ranks = {}
        
        rank = 1
        
        for num in copy:
            ranks[num] = rank
            rank += 1
        
        ans = []
        
        for num in arr:
            ans.append(ranks[num])
        
        return ans
