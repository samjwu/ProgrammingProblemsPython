class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        set1 = self.getSet(word1)
        set2 = self.getSet(word2)
        
        if set1 != set2:
            return False
        
        freq1 = self.getFreq(word1)
        freq2 = self.getFreq(word2)
        
        counts1 = self.getCounts(freq1)
        counts2 = self.getCounts(freq2)
        
        return counts1 == counts2
        
    def getSet(self, word: str) -> set[int]:
        wordSet = set()
        
        for c in word:
            wordSet.add(c)
        
        return wordSet
        
    def getFreq(self, word: str) -> list[int]:
        freq = [0 for i in range(26)]
        
        for c in word:
            freq[ord(c) - ord('a')] += 1
            
        return freq
    
    def getCounts(self, freq: list[int]) -> dict[int, int]:
        counts = defaultdict(int)
        
        for i in range(26):
            counts[freq[i]] += 1
            
        return counts
