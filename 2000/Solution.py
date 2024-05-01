class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        
        idx = -1
        
        for i in range(n):
            if ch == word[i]:
                idx = i
                break
                
        if idx == -1:
            return word
        
        ans = ""
        
        for i in range(idx, -1, -1):
            ans += word[i]
            
        return ans + word[idx+1:]
