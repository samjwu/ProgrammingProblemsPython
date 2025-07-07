class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        if not n >= 3 or not word.isalnum():
            return False

        vowels = "aeiouAEIOU"
        has_vowel = False
        has_consonant = False

        for c in word:
            if c.isdigit():
                continue
            elif c in vowels:
                has_vowel = True
            else:
                has_consonant = True

        return has_vowel and has_consonant
