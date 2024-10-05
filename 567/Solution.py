class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        if m > n:
            return False
        
        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]
        
        for i in range(m):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
            
        for i in range(m, n):
            if self.equalFreq(freq1, freq2):
                return True
            
            freq2[ord(s2[i-m]) - ord('a')] -= 1
            freq2[ord(s2[i]) - ord('a')] += 1
            
        
        if self.equalFreq(freq1, freq2):
            return True
        
        return False
    
    def equalFreq(self, freq1: list[int], freq2: list[int]) -> bool:
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
            
        return True
