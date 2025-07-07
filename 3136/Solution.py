class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        if not n >= 3 or not word.isalnum():
            return False

        vowels = "aeiouAEIOU"
        has_vowel = any(c in vowels for c in word if not c.isdigit())
        has_consonant = any(c.isalpha() and c not in vowels for c in word if not c.isdigit())

        return has_vowel and has_consonant
