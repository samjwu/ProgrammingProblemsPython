class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
            
        return ""
    
    def isPalindrome(self, word: str) -> bool:
        n = len(word)
        
        for i in range(n // 2):
            if word[i] != word[n-1 - i]:
                return False
        
        return True
