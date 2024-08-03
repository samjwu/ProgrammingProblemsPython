class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq1 = Counter(target)
        
        freq2 = Counter(arr)
        
        return freq1 == freq2
