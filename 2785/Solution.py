class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_indices = []
        vowels = []
        
        for i in range(len(s)):
            if self.isVowel(s[i]):
                vowel_indices.append(i)
                vowels.append(s[i])
                
        vowels.sort()
        
        ans = [c for c in s]
        
        for i in range(len(vowels)):
            ans[vowel_indices[i]] = vowels[i]
            
        return "".join(ans)
        
    def isVowel(self, c: str) -> bool:
        return c in "aeiouAEIOU"
