class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        min_length = n >= 3
        has_valid_chars = word.isalnum()

        if not min_length or not has_valid_chars:
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
