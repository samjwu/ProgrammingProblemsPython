class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        
        n = len(words)
        
        for i in range(n):
            word = words[i]
            
            if word.find(searchWord, 0) == 0:
                return i+1
            
        return -1
