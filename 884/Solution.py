class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        freq = defaultdict(int)
        
        for word in words1:
            freq[word] += 1
            
        for word in words2:
            freq[word] += 1
            
        ans = []
        
        for word in freq:
            if freq[word] == 1:
                ans.append(word)
                
        return ans
