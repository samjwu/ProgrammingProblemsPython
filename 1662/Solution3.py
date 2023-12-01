class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        chars1 = self.generate(word1)
        chars2 = self.generate(word2)
        
        for c1, c2 in zip(chars1, chars2):
            if c1 != c2:
                return False
            
        return True

    def generate(self, words: List[str]) -> Generator[str, None, None]:
        for word in words:
            for c in word:
                yield c
                
        yield None
