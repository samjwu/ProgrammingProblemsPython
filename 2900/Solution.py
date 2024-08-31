class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        
        n = len(groups)
        
        idx = 1
        
        prev = groups[0]
        
        ans.append(words[0])
        
        while idx < n:
            if groups[idx] != prev:
                ans.append(words[idx])
                prev = groups[idx]
                
            idx += 1
            
        return ans
