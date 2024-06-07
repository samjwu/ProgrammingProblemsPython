class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        
        words = sentence.split(" ")
        
        n = len(words)
        
        for i in range(n):
            for root in dictionary:
                if words[i].find(root) == 0:
                    words[i] = root
                    break
        
        return " ".join(words)
                    