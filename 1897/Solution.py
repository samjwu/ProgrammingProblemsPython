class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        
        freq = defaultdict(int)
        
        for word in words:
            for c in word:
                freq[c] += 1
                
        for i in range(26):
            c = chr(ord("a") + i)
            
            if freq[c] % n != 0:
                return False
            
        return True
