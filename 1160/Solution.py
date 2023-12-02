class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = [0 for i in range(26)]
        
        for c in chars:
            freq[ord(c) - ord('a')] += 1
            
        ans = 0
            
        for word in words:
            if self.is_good(word, freq):
                ans += len(word)
                
        return ans
    
    def is_good(self, word: str, freq: Dict[str, int]) -> bool:
        word_chars = [0 for i in range(26)]
        
        for c in word:
            word_chars[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if freq[i] < word_chars[i]:
                return False
            
        return True
