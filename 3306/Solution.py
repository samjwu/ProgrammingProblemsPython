class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        
        left = 0
        right = 0

        vowel_count = {}
        consonant_count = 0
        
        # next_consonant[i] = index of consonant after ith char
        next_consonant = [0] * n
        consonant_idx = n

        for i in range(n - 1, -1, -1):
            next_consonant[i] = consonant_idx

            if not self.is_vowel(word[i]):
                consonant_idx = i

        while right < n:
            c = word[right]

            if self.is_vowel(c):
                vowel_count[c] = vowel_count.get(c, 0) + 1
            else:
                consonant_count += 1

            # shrink window if too many consonants
            while (consonant_count > k):
                c_left = word[left]
                
                if self.is_vowel(c_left):
                    vowel_count[c_left] -= 1
                    if vowel_count[c_left] == 0:
                        del vowel_count[c_left]
                else:
                    consonant_count -= 1

                left += 1

            # count valid answers
            while (
                left < n
                and len(vowel_count) == 5
                and consonant_count == k
            ):
                # include all substrings with extra vowels
                # cutoff is obtained at the first extra consonant
                ans += next_consonant[right] - right

                c_left = word[left]

                if self.is_vowel(c_left):
                    vowel_count[c_left] -= 1
                    if vowel_count[c_left] == 0:
                        del vowel_count[c_left]
                else:
                    consonant_count -= 1

                left += 1

            right += 1

        return ans

    def is_vowel(self, c: str) -> bool:
        return c in "aeiou"

    